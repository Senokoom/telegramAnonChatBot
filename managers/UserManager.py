from managers.DataManager import DataManager
from classes.classUser import User


class UserManager:
    def __init__(self):
        self.dataManager = DataManager()
        self.usersList = self.dataManager.get_all_users()

    def get_user_by_id(self, user_id):
        return self.dataManager.get_user_by_id(user_id)


    def create_and_save_user(self, user_dict: dict):
        user = User(**user_dict)
        if self.dataManager.get_user_by_id(user.id):
            return user
        else:
            return self.dataManager.save_user(user)





