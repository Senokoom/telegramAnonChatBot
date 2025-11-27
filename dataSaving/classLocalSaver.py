from classes.classUser import User
from classes.classBan import Ban
from classes.classReport import Report
from settings.settings import local_user_save_path, local_report_save_path, local_ban_save_path
import csv


class LocalSaver:
    def __init__(self):
        self.user_save_path = local_user_save_path
        self.report_save_path = local_report_save_path
        self.ban_save_path = local_ban_save_path

    def save_user(self, user: User):
        """
        Сохраняет данные user в файле csv
        :param user: объект класса User
        :return: True при успешном создании, False при ошибке
        """
        user_dict_data = user.toDict()
        try:
            if self.get_user_by_id(user.userid):
                return "Was already in the system"
            with open(self.user_save_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=user_dict_data)
                writer.writeheader()
                return "Successful"
        except Exception as e:
            return e

    def get_user_by_id(self, userid: str) -> User | Exception:
        """
        :param userid: уникальный id пользователя
        :return: Возвращает объет класса User или None. Если пользователя не существует.
        """
        try:
            with open(self.user_save_path, mode='r', encoding='utf-8') as userdata_file:
                userdata = csv.DictReader(userdata_file)
                for row in userdata:
                    if row['userid'] == userid:
                        return User(row["userid"], row["name"], row["age"], row["sex"], row["tags"], row["location"])
        except Exception as e:
            return e

    def save_report(self, report: Report) -> True | Exception:
        """
        Сохраняет данные report в файле csv
        :param report: объект класса Report
        :return: True при успешном создании, False при ошибке
        """
        report_dict_data = report.toDict()
        try:
            with open(self.report_save_path, mode='w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=report_dict_data)
                writer.writeheader()
                return True
        except Exception as e:
            return e

    def get_all_reports(self) -> list[Report] | Exception:
        """
        :return: возвращает массив объектов класса Report
        """
        try:
            with open(self.report_save_path, mode='r', encoding='utf-8') as reportdata_file:
                reportdata = csv.DictReader(reportdata_file)
                reports_list = []
                for row in reportdata:
                    reports_list.append(Report(row["id"], row["userid"], row["reason"], row["severity"]))
                return reports_list
        except Exception as e:
            return e

    def save_ban(self, ban: Ban) -> True | Exception:
        """
        Добавляет Ban в файл
        :param ban: объект класса Ban
        :return:
        """
        ban_dict_data = ban.toDict()
        try:
            with open(self.ban_save_path, mode='w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=ban_dict_data)
                writer.writeheader()
                return True
        except Exception as e:
            return e

    def get_all_bans(self) -> list[Ban] | Exception:
        """
        :return: возвращает list из объект класса Ban
        """
        try:
            with open(self.ban_save_path, mode='r', encoding='utf-8') as bandata_file:
                bandata = csv.DictReader(bandata_file)
                bans_list = []
                for row in bandata:
                    bans_list.append(Ban(row["id"], row["userid"], row["reason"], row["date"], row["duration"]))
                return bans_list
        except Exception as e:
            return e
