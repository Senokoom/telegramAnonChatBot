from classBan import Ban
from classDatabase import Database


class BanManager:
    """
    Класс отвечающий за управления Блокировками.
    Хранит словарь всех блокировок по id блокировки.(не список, потому что скорость поиска по словарю выше и изменять удобнее)
    Позволяет посмотреть блокировки по id блокировки/пользователя или добавить/создать блокировку
    """

    def __init(self, database: Database):
        """
        Менеджер для управления блокировками.
        :param database: база данных пользователей с которой работаешь
        """
        self.database = database
        self.bans: dict[str, Ban] = self.database.get_all_bans()

    def check_user_by_id(self, userid: str) -> Ban | bool | None:
        """
        проверяет наличие активных блокировок у пользователя по id.
        :param userid: уникальный id пользователя
        :returns: объект класса Ban, текущую активную блокировку. False, если нету активной. None если id нету в базе
        """
        user = self.database.get_user_by_id(userid)
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
