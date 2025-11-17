import uuid

from classes.classBan import Ban
from datetime import timedelta
from DataManager import DataManager


class BanManager:
    """
    Класс отвечающий за управления Блокировками.
    Хранит словарь всех блокировок по id блокировки.(не список, потому что скорость поиска по словарю выше и изменять удобнее)
    Позволяет посмотреть блокировки по id блокировки/пользователя или добавить/создать блокировку
    """

    def __init(self, dataManager: DataManager):
        """
        Менеджер для управления блокировками.
        :param dataManager: база данных пользователей с которой работаешь
        """
        self.dataManager = dataManager
        self.bans: dict[str, Ban] = self.dataManager.get_all_bans()

    def check_user_by_id(self, userid: str) -> Ban | bool | None:
        """
        проверяет наличие активных блокировок у пользователя по id.
        :param userid: уникальный id пользователя
        :returns: объект класса Ban, текущую активную блокировку. False, если нету активной. None если id нету в базе
        """
        user = self.dataManager.get_user_by_id(userid)
        if user is None:
            return None
        elif user.bans is None:
            return False
        else:
            for ban in user.bans:
                if ban.is_active():
                    return ban
            return False

    def get_ban_by_id(self, banid: str) -> Ban | None:
        """
        Находит ban в списке.
        :param banid: уникальный id блокировки
        :return: объект класса classBan, или None
        """
        ban = self.bans.get(banid)
        if ban is None:
            return None
        else:
            return ban

    def create_ban(self, reason: str, userid, duration: timedelta) -> Ban:
        """
        Создает Ban и кидает его в бд
        :param reason: причина
        :param userid: id пользователя
        :param duration: длительность timedelta
        :return: объект класса Ban
        """
        ban = Ban(uuid.uuid4(), reason, userid, duration)
        self.dataManager.insert_ban(ban)
        return ban

    def ban_user_by_id(self, userid, reason: str, duration: timedelta) -> str:
        """
        Кидает блокировку на пользователя User по id
        :param reason: Причина блокировки str.
        :param userid: уникальный id пользователя
        :param duration: Длительность блокировки timedelta
        :return: str информацию о только что созданном Ban
        """
        user = self.dataManager.get_user_by_id(userid)
        user.bans.append(self.create_ban(reason, userid, duration))
        return user.bans[-1].info()

