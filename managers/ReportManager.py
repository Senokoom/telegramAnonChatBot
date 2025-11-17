import uuid

from classes.classReport import Report
from DataManager import DataManager


class ReportManager:
    """
      Класс отвечающий за управления репортами.
      Хранит словарь всех репортов по id репотра.
      Хранит словать всех блокировок по id пользователей.
      Позволяет посмотреть репотры по id репорта/пользователя или добавить/создать блокировку
      """

    def __init__(self, dataManager: DataManager):
        """
        Менеджер для управления репортами
        :param dataManager: База данных пользователей
        """
        self.dataManager = dataManager
        self.reports: dict[str, Report] = self.dataManager.get_all_reports()

    def check_user_by_id(self, userid: str) -> list[Report] | bool | None:
        """
        проверяет наличие репортов у пользователя по id.
        :param userid: уникальный id пользователя
        :returns: list[Reports], если есть. False, если нету. None если id нету в базе
        """
        user = self.dataManager.get_user_by_id(userid)
        if user is None:
            return None
        elif user.reports is None:
            return False
        else:
            return user.reports

    def create_report(self, userid, reason, severity) -> Report:
        """
        Создает репорт и записывает его в бд
        :param userid: id пользователя
        :param reason: причина
        :param severity: тяжесть, от нее зависит скорость рассмотрения жалобы
        :return: объект класса Report
        """
        report = Report(uuid.uuid4(), userid, reason, severity)
        self.dataManager.insert_report(report)
        return report

    def report_user_by_id(self, userid, reason, severity) -> str:
        """
        Кидает блокировку Report по id пользователя
        :param userid: id пользователя
        :param reason: причина
        :param severity: тяжесть
        :return:
        """
        user = self.dataManager.get_user_by_id(userid)
        user.reports.append(self.create_report(userid, reason, severity))
        return user.reports[-1].info()

