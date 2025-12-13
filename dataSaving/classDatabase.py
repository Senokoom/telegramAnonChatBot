from classes.classUser import User
from classes.classBan import Ban
from classes.classReport import Report


class Database:
    def __init__(self):
        pass

    def get_user_by_id(self, userid: str) -> User:
        """
        :param userid: уникальный id пользователя
        :return: Возвращает объет класса User или None. Если пользователя не существует.
        """
        pass

    def save_user(self, user: dict):
        """
        Сохраняет user базу данных
        :param user: объект класса User
        :return: True при успешном создании, False при ошибке
        """
        pass


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
