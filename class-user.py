import classReport, classBan

class user:
    def __init__(self, tgid, name, age, sex, tags: list,
                  current_status, location: str = None, is_admin: bool = False):
        """
        **Создает нового пользователя**\n
        *tgid* - id Telegram пользователя ***(неизменяемое)***\n
        *name* - Имя пользователя. Default имя пользователя в Telegram\n
        *age* - Возраст пользователя\n
        *sex* - пол пользователя (M, F, None)\n
        *tags* - теги пользователя для поиска собеседника  (пока не придумал)\n
        *current_status* - статус пользователя в системе (offline, online, in_chat, banned)\n
        *location* - геолокация пользователя, хранит в себе только город\n
        *connected_to* - указан другой user с которым пользователь общается\n
        *comment* - комментарий на пользователе, видит только admin\n
        *is_admin* - является ли пользователь администратором (True, False)\n
        *reports* - жалобы на пользователя\n
        *bans* - блокировки пользователя\n
        *log* - log именно этого пользователя
        """
        
        self.tgid = tgid
        self.name = name
        self.age = age
        self.sex = sex
        self.location = location
        self.tags = tags
        self.current_status = current_status
        self.connected_to: user = None
        self.comment: str = ''
        self.is_admin = is_admin
        self.reports: list[classReport.report] = None
        self.bans: list[classBan.ban] = None
        self.log: list = None
    
    def info(self):
        """
        Выводит в консоль **данные**(*tgid, name, age, sex, current_status, comment, reports, bans*) пользователя
        """
        print(f"Tgid: {self.tgid}\n"
              f"Name: {self.name}\n"
              f"Age: {self.age}\n"
              f"Sex: {self.sex}\n"
              f"Current status: {self.current_status}\n"
              f"Comment: {self.comment}\n"
              f"Reports: {[x.info() for x in self.reports] if self.reports else "Нет репортов"}\n"
              f"Bans: {[x.info for x in self.bans()] if self.bans else "Нет блокировок"}")
    

    def modify_comment(self, text, admin_right):
        """
        Позволяет добавить/изменить комментарий к пользователю. Может видеть и изменять только admin
        """
        if(admin_right):
            self.comment = text
        else:
            print("У вас недостаточно прав для этого действия")


    def log(self):
        """
        Выводит **log** пользователя в консоль
        """
        for x in self.log:
            print(x)
        pass