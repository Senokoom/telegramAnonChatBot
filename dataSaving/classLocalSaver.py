from classes.classUser import User
from classes.classBan import Ban
from classes.classReport import Report
from settings.settings import local_user_save_path, local_report_save_path, local_ban_save_path, local_backup_time, local_backup_path
import time
from datetime import datetime
import shutil
import csv


class LocalSaver:
    def __init__(self):
        self.user_save_path = local_user_save_path
        self.report_save_path = local_report_save_path
        self.ban_save_path = local_ban_save_path
        self.backup_time = local_backup_time
        self.backup_path = local_backup_path

    def save_user(self, user_dict_data: dict):
        """
        Сохраняет данные user в файле csv
        :param user_dict_data: класс dict. user.todict()
        :return: True, если успешно. Exception если нет
        """
        try:
            if self.get_user_by_id(user_dict_data['userid']):
                return "Was already in the system"
            with open(self.user_save_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=user_dict_data)
                writer.writeheader()
                return True
        except Exception as e:
            return e

    def get_user_by_id(self, userid: str) -> User | Exception:
        """
        :param userid: уникальный id пользователя
        :return: Возвращает объет класса User или Exception. Если пользователя не существует.
        """
        try:
            with open(self.user_save_path, mode='r', encoding='utf-8') as userdata_file:
                userdata = csv.DictReader(userdata_file)
                for row in userdata:
                    if row['userid'] == userid:
                        return User(row["userid"], row["name"], row["age"], row["sex"], row["tags"], row["location"])
        except Exception as e:
            return e

    def save_report(self, report_dict_data: dict) -> True | Exception:
        """
        Сохраняет данные report в файле csv
        :param report_dict_data: объект dict. report.todict()
        :return: True при успешном создании, Exception если нет
        """
        try:
            with open(self.report_save_path, mode='w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=report_dict_data)
                writer.writeheader()
                return True
        except Exception as e:
            return e

    def get_all_reports(self) -> list[Report] | Exception:
        """
        :return: возвращает массив объектов класса Report или Exception
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

    def save_ban(self, ban_dict_data: dict) -> True | Exception:
        """
        Добавляет Ban в файл
        :param ban_dict_data: класс dict. Получается если ban.todict()
        :return: True or Exception
        """
        try:
            with open(self.ban_save_path, mode='w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=ban_dict_data)
                writer.writeheader()
                return True
        except Exception as e:
            return e

    def get_all_bans(self) -> list[Ban] | Exception:
        """
        :return: возвращает list из объект класса Ban or Exception
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

    def backup(self):
        """
        Создает бэкап копии для user через заданный интервал
        Так как report и ban еще не имеют реализации, то нет смысла делать их бэкап
        :return:
        """
        while True:
            try:
                backupfile_path = f"{self.backup_path}\\local_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
                shutil.copy(self.user_save_path, backupfile_path)
                time.sleep(self.backup_time)
            except Exception as e:
                return e


