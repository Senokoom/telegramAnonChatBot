from DataManager import DataManager
from classes.classUser import User


class UserManager:
    def __init__(self, dataManager: DataManager):
        self.dataManager = dataManager
        self.usersList = dataManager.get_all_users()

    def check_if_user_in_database_by_id(self, user_id):
        return self.dataManager.get_user_by_id(user_id)




