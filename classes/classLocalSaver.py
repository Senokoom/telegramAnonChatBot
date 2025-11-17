from classUser import User
from classBan import Ban
from classReport import Report


class LocalSaver:
    def __init__(self):
        pass

    def get_user_by_id(self, userid: str) -> User:
        """
        :param userid: уникальный id пользователя
        :return: Возвращает объет класса User или None. Если пользователя не существует.
        """
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

    def insert_ban(self, ban: Ban):
        """
        Добавляет Ban в базу данных
        :param ban: объект класса Ban
        :return:
        """
        pass

    def insert_report(self, report: Report):
        """
        Добавляет Report в базу данных
        :param report: объект класса Report
        :return:
        """
        pass