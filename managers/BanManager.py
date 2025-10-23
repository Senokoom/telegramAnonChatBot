import classBan
class banManager:
    """
    Класс отвечающий за управления Блокировками.
    Хранит словарь всех блокировок по id блокировки.(не список, потому что скорость поиска по словарю выше и изменять удобнее)
    Хранит словать всех блокировок по id пользователей.
    Позволяет посмотреть блокировки по id пользователя или добавить/создать блокировку
    """

    def __init(self):
        self.bans: dict[str, classBan] = {}
        self.bans_by_userid: dict[str, classBan] = {}

    def check_user_by_id(self, userid: str) -> bool | str:
        """
        проверяет наличие активных блокировок у пользователя по id.
        :param userid: уникальный id пользователя
        :returns: True, если есть актинвые. False, если нету. Или "Пользователя не существует", если id нету в базе
        """

        bans = self.bans_by_userid.get(userid)
        if bans is None:
            return False
        else:
            for ban in bans:
                if ban.is_active():
                    return True
            return False
