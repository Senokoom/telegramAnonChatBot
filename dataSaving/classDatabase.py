import sqlalchemy.exc
from sqlalchemy import Column, ForeignKey

from classes.classUser import User
from classes.classBan import Ban
from classes.classReport import Report
import sqlalchemy as sa
from sqlalchemy import String, Integer, Float, Boolean, CHAR, JSON, DATETIME, Interval, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker, relationship, selectinload


#cursor.execute("PRAGMA foreign_keys=ON") ДЛЯ ПРОВЕРКИ FOREIGN_KEYS

class Base(DeclarativeBase):
    pass

class DbUser(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    sex = Column(CHAR)
    location = Column(String)
    is_admin = Column(Boolean)
    tags = Column(JSON, default=list)
    current_status = Column(String)
    connected_to_id = Column(String, nullable=True, default=None, index=True)
    comment = Column(String)
    bans = relationship("DbBan", back_populates="user", cascade="all, delete-orphan", lazy="selectin")
    reports = relationship("DbReport", back_populates="user", cascade="all, delete-orphan", lazy="selectin", foreign_keys="[DbReport.user_id]")
    log = Column(JSON, default=list)

class DbBan(Base):
    __tablename__ = "bans"
    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id", ondelete="CASCADE"), index=True)
    reason = Column(String)
    user = relationship("DbUser", back_populates="bans")
    date = Column(DATETIME)
    duration = Column(Interval)

class DbReport(Base):
    __tablename__ = "reports"
    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id", ondelete="CASCADE"), index=True)
    user = relationship("DbUser", back_populates="reports", foreign_keys=[user_id])
    from_user_id = Column(String, ForeignKey("users.id"))
    comment = Column(String)
    reason = Column(String)


class Database:

    def __init__(self, db_url = "sqlite:///my_database.db"):
        self.engine = sa.create_engine(db_url, echo=False, connect_args={"timeout": 30})
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(self.engine)



    def db_class_to_target_class(self, db_obj: DbBan | DbReport, target_cls: type[Ban] | type[Report]) -> Ban | Report | None:
        """
        Переделывает из базы данных в норм класс
        :param db_obj: Класс полученный из БД
        :param target_cls: Класс в который нужно перевести
        :return: Объект класса, который нам нужен :)
        """
        if db_obj is None:
            return None
        data = {
            col.name: getattr(db_obj, col.name) for col in db_obj.__table__.columns
        }
        return target_cls(**data)

    def target_class_to_db_class(self, obj, db_cls):
        """
          Переводит Ban -> DbBan или Report -> DbReport
          """
        if obj is None:
            return None
        # Берем только те поля из объекта, которые реально есть как колонки в таблице БД
        col_names = {col.name for col in db_cls.__table__.columns}
        data = {k: v for k, v in vars(obj).items() if k in col_names}
        return db_cls(**data)


    def user_to_db_user(self, user: User) -> DbUser:
        """
          Переводит User -> DbUser вместе со списками bans и reports
          """
        col_names = {col.name for col in DbUser.__table__.columns}
        data = {k: v for k, v in vars(user).items() if k in col_names}
        data["bans"] = [
            self.target_class_to_db_class(b, DbBan) for b in (user.bans or [])
        ]
        data["reports"] = [
            self.target_class_to_db_class(r, DbReport) for r in (user.reports or [])
        ]

        return DbUser(**data)


    def db_user_to_user(self, db_user: DbUser) -> User | None:
        """
        Переделывает DbUser базы данных в User
        :param db_user: DbUser из базы данных
        :return: Объект класса User или None
        """
        if db_user is None:
            return None
        data = {
            col.name: getattr(db_user, col.name) for col in db_user.__table__.columns
        }
        data["bans"] = [self.db_class_to_target_class(b, Ban) for b in db_user.bans]
        data["reports"] = [self.db_class_to_target_class(r, Report) for r in db_user.reports]
        return User(**data)


    def get_user_by_id(self, user_id: str) -> User | None:
        """
        :param user_id: уникальный id пользователя
        :return: Возвращает объет класса User или None. Если пользователя не существует.
        """
        with self.Session() as session:
            stmt = select(DbUser).options(selectinload(DbUser.bans), selectinload(DbUser.reports)).where(DbUser.id == user_id)
            user = session.execute(stmt).scalar_one_or_none()
            return self.db_user_to_user(user)


    def save_user(self, user: User):
        """
        Сохраняет user базу данных
        :param user: объект класса User
        :return: True при успешном создании, False при ошибке
        """
        db_user = self.user_to_db_user(user)
        if db_user:
            try:
                with self.Session() as session:
                    with session.begin():
                        session.merge(db_user)
                        return True
            except sqlalchemy.exc.SQLAlchemyError as e:
                print(f"Ошибка в БД {e}")
                return False


    def get_all_users(self):
        pass


    def get_all_reports(self) -> dict[str, Report]:
        """
        :return: возвращает словарь, где key - report.id, а value - объект класса Report
        """
        pass

    def get_all_bans(self) -> dict[str, Ban]:
        """
        :return: возвращает словарь, где key - ban.id, а value - объект класса Ban
        """
        pass

    def save_ban(self, ban: dict):
        """
        Добавляет Ban в базу данных
        :param ban: объект класса Ban
        :return:
        """
        pass

    def save_report(self, report: dict):
        """
        Добавляет Report в базу данных
        :param report: объект класса Report
        :return:
        """
        pass


from datetime import datetime, timedelta
db = Database()
test_user = User(
    id="tg_100500",
    name="тестик",
    age=24,
    sex="M",
    tags=["игры", "музыка"],
    location="Москва",
    is_admin=True,
)
test_user.bans.append(
    Ban(
        id="ban_1",
        user_id="tg_100500",
        date=datetime.now(),
        reason="тест",
        duration=timedelta(days=7),
    )
)

# Сохраняем
ok = db.save_user(test_user)
print("Сохранено:", ok)

# Достаем обратно из БД
loaded_user = db.get_user_by_id("tg_100500")
print(f"Загружен: {loaded_user.name}, админ: {loaded_user.is_admin}")
print(
    f"Баны ({len(loaded_user.bans)} шт.): до"
    f" {loaded_user.bans[0].date + loaded_user.bans[0].duration}"
)