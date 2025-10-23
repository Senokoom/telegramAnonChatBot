from classReport import Report
from classDatabase import Database


class ReportManager:
    """
      Класс отвечающий за управления репортами.
      Хранит словарь всех репортов по id репотра.
      Хранит словать всех блокировок по id пользователей.
      Позволяет посмотреть репотры по id репорта/пользователя или добавить/создать блокировку
      """

    def __init__(self, database: Database):
        """
        Менеджер для управления репортами
        :param database: База данных пользователей
        """
        self.database = database
        self.reports: dict[str, Report] = self.database.get_all_reports()

    def check_user_by_id(self, userid: str) -> list[Report]| bool | None:
        """
        проверяет наличие репортов у пользователя по id.
        :param userid: уникальный id пользователя
        :returns: list[Reports], если есть. False, если нету. None если id нету в базе
        """
        user = self.database.get_user_by_id(userid)
        if user is None:
            return None
        elif user.reports is None:
            return False
        else:
            return user.reports
