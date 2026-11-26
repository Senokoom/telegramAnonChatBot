import logger
from dataSaving.classLocalSaver import LocalSaver
from dataSaving.classDatabase import Database
from classes.classUser import User, Ban, Report
from logger import Log

class DataManager:
    def __init__(self):
        self.local = LocalSaver()
        self.database = Database()
        self.log = logger.Log("datamanager", "data").logger
        self.log.info(
            "---------------------------------------------NEW SESSION----------------------------------------------------")

    def save_user(self, user: User):
        """
        Сохраняет User локально и в базу данных.
        Возвращает False либо объект класса User.
        :param user: объект класса User
        """
        self.log.info("Пытаюсь сохранить пользователя в память")
        try:
            user_dict = user.toDict()
            self.local.save_user(user_dict)
            self.database.save_user(user)
            return user
        except Exception as e:
            self.log.error(f"Не получилось сохранить юзера: {e}")
            return False


    def get_user_by_id(self, userid):
        """
        возвращает объект класса User
        :param userid: уникальный id пользователя
        :return: объект класса User
        """
        self.log.info("Получаю User по id")
        return self.database.get_user_by_id(userid)

    def get_all_users(self):
        """
        :return: всех user в базе данных
        """
        self.log.info("Получаю всех User")
        return self.database.get_all_users()

    def get_all_bans(self):
        """
        :return:
        """
        self.log.info("Получаю все Ban")
        return self.database.get_all_bans()

    def get_all_reports(self):
        self.log.info("Получаю все Report")
        return self.database.get_all_reports()

    def insert_ban(self, ban: Ban):
        """
        Сохраняет в базу данных и локально
        :param ban:  объект класса Ban
        :return: массив с результатом сохраниения [local, database]
        """
        self.log.info("Сохраняю Ban в память")
        ban_dict = ban.toDict()
        loc_res = self.local.save_ban(ban_dict)
        db_res = self.database.save_ban(ban_dict)
        return [loc_res, db_res]

    def insert_report(self, report: Report):
        """
        Сохраняет в базу данных и локально
        :param report:  объект класса Report
        :return: массив с результатом сохраниения [local, database]
        """
        self.log.info("Сохраняю Report в память")
        report_dict = report.toDict()
        loc_res = self.local.save_report(report_dict)
        db_res = self.database.save_report(report)
        return [loc_res, db_res]

    def from_local_to_db(self):
        """
        из локального файла сохраняет все в базу данных
        :return: результат выполнения(true, exception)
        """
        pass
