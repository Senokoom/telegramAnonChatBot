from classes.classLocalSaver import LocalSaver
from classes.classDatabase import Database
from classes.classUser import User


class DataManager:

    def __init__(self, local: LocalSaver, database: Database):
        self.local = local
        self.database = database

    def save_user(self, user: User):
        pass

    def get_user_by_id(self, userid):
        pass

    def get_all_users(self):
        pass

    def get_all_bans(self):
        pass

    def get_all_reports(self):
        pass

    def insert_ban(self, ban):
        pass

    def insert_report(self, report):
        pass
