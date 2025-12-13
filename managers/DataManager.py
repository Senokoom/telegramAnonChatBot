from dataSaving.classLocalSaver import LocalSaver
from dataSaving.classDatabase import Database
from classes.classUser import User, Ban, Report


class DataManager:
    def __init__(self):
        self.local = LocalSaver()
        self.database = Database()

    def save_user(self, user: User):
        """
        Сохраняет User локально и в базу данных.
        Возвращает массив с результатом сохранения
        :param user: объект класса User
        """
        user_dict = user.toDict()
        loc_res = self.local.save_user(user_dict)
        db_res = self.database.save_user(user_dict)
        return [loc_res, db_res]

    def get_user_by_id(self, userid):
        """
        возвращает объект класса User
        :param userid: уникальный id пользователя
        :return: объект класса User
        """
        return self.database.get_user_by_id(userid)

    def get_all_users(self):
        """
        :return: всех user в базе данных
        """
        return self.database.get_all_users()

    def get_all_bans(self):
        """
        :return:
        """
        return self.database.get_all_bans()

    def get_all_reports(self):
        return self.database.get_all_reports()

    def insert_ban(self, ban: Ban):
        """
        Сохраняет в базу данных и локально
        :param ban:  объект класса Ban
        :return: массив с результатом сохраниения [local, database]
        """
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
        report_dict = report.toDict()
        loc_res = self.local.save_report(report_dict)
        db_res = self.database.save_report(report_dict)
        return [loc_res, db_res]

    def from_local_to_db(self):
        """
        из локального файла сохраняет все в базу данных
        :return: результат выполнения(true, exception)
        """

