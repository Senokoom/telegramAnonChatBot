from DataManager import DataManager
from classes.classUser import User


class UserManager:
    def __init__(self, dataManager: DataManager):
        self.dataManager = dataManager
        self.usersList = dataManager.get_all_users()


