from dataSaving.classLocalSaver import LocalSaver
from dataSaving.classDatabase import Database
from classes.classUser import User


class DataManager:
    def __init__(self):
        self.local = LocalSaver()
        self.database = Database()
        self.up_to_date()

    def save_user(self, user: User):
        """
        Сохраняет User локально и в базу данных.
        Возвращает массив с результатом сохранения
        :param user: объект класса User
        """
        loc_res = self.local.save_user(user)
        db_res = self.database.save_user(user)
        return [loc_res, db_res]

    def get_user_by_id(self, userid):
        """
        возвращает объект класса User
        :param userid: уникальный id пользователя
        :return: объект класса User
        """
        db_res = self.database.get_user_by_id(userid)
        return db_res

    def get_all_users(self):
        """
        Возвращает всех user
        :return:
        """
        return self.database.get_all_users()

    def get_all_bans(self):
        """

        :return:
        """
        return self.database.get_all_bans()

    def get_all_reports(self):
        return self.database.get_all_reports()

    def insert_ban(self, ban):
        loc_res = self.local.save_ban(ban)
        db_res = self.database.save_ban(ban)
        return [loc_res, db_res]

    def insert_report(self, report):
        loc_res = self.local.save_report(report)
        db_res = self.database.save_report(report)
        return [loc_res, db_res]

    def up_to_date(self):
        """
        проверяет где больше записей, а потом синхронизирует (???)
        хз пока как тут сделать :(
        :return:
        """
        pass
