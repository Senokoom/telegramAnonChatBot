from classReport import Report
from classBan import Ban
# noinspection SpellCheckingInspection


class User:
    def __init__(self, userid, name, age, sex, tags: list, location: dict = None):
        """
        **Создает нового пользователя**\n
        *userid* - id пользователя **(неизменяемое)** \n
        *name* - Имя пользователя. Default имя пользователя в Telegram\n
        *age* - Возраст пользователя\n
        *sex* - пол пользователя (M, F, None)\n
        *tags* - теги пользователя для поиска собеседника  (пока не придумал)\n
        *current_status* - статус пользователя в системе (offline, searching, in_chat)\n
        *location* - геолокация пользователя, хранит в себе только город\n
        *connected_to* - указан другой user с которым пользователь общается\n
        *comment* - комментарий на пользователе, видит только admin\n
        *is_admin* - является ли пользователь администратором (True, False)\n
        (этого нет)*reports* - жалобы на пользователя\n
        (этого нет)*bans* - блокировки пользователя\n
        *log* - log именно этого пользователя
        """

        self.userid = userid
        self.name = name
        self.age = age
        self.sex = sex
        self.location = location
        self.tags = tags
        self.current_status = None
        self.connected_to: User | None = None
        self.comment: str = ''
        # self.reports: list[Report] = []
        # self.bans: list[Ban] = []
        self.log: list = []

    def info(self):
        """
        выводит в консоль **данные** пользователя (*userid, name, age, sex, comment, reports, bans*)
        """

        return print(
            f"Userid: {self.userid}\n"
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Sex: {self.sex}\n"
            # f"Current status: {self.current_status}\n" тоже пока убрал
            f"Comment: {self.comment}\n"
            # f"Reports: {[x.info() for x in self.reports] if self.reports else 'Нет репортов'}\n" и их тож убрал
            # f"Bans: {[x.info for x in self.bans] if self.bans else 'Нет блокировок'}" их убрал
            )

    def setup(self, name: str, age: int, sex: str, location: dict, tags: list):
        """
                Настройка аккаунта пользователя. Позволяет поменять **Имя, Возраст, Пол, Геолокацию, Теги**

                пока что только через консоль
                """
        ''' Всю эту логику надо перенести в другое место (в основной файл) тут она излишняя
        
        self.name = self.name if ((name_inp := input("Введите имя или пропустите(skip): ")).lower() == "skip") \
            else name_inp
        # использовал тут оператор моржа и тернарную запись if. Сложна, но прикольна
        while ((not (age_inp := input("Введите возвраст или пропустите(skip): ")).isdigit())
               and age_inp.lower() != "skip"):
            print(f"Введено некорректное значение")
        # запись в возраст прост гениальная :)
        self.age = self.age if age_inp == "skip" else int(age_inp)
        # self.sex =
        # чел может выбрать из 3х вариантов 1.
        # Хз как сделать это в python консоли, но в тг будет проще т.к. там просто кнопки сделать можно
        while (((location_inp := input("Введите из какого вы города или пропустите(skip): ")) != "skip")
               and not (location_dict := city_isreal(location_inp))):
            pass
        self.location = self.location if self.location == "skip" else location_dict
        '''
        self.name = name
        self.age = age
        self.sex = sex
        self. location = location
        self.tags = tags

    def modify_comment(self, text, is_admin: bool):
        """
        Позволяет добавить/изменить комментарий к пользователю. Может видеть и изменять только admin
        """
        if is_admin:
            self.comment = text
        else:
            print("У вас недостаточно прав для этого действия")

    def log(self):
        """

        Выводит **log** пользователя в консоль
        """
        for x in self.log:
            print(x)

        # **Создает нового пользователя**\n
        # *userid* - id пользователя **(неизменяемое)** \n
        # *name* - Имя пользователя. Default имя пользователя в Telegram\n
        # *age* - Возраст пользователя\n
        # *sex* - пол пользователя (M, F, None)\n
        # *tags* - теги пользователя для поиска собеседника  (пока не придумал)\n
        # *current_status* - статус пользователя в системе (offline, online, in_chat, banned)\n
        # *location* - геолокация пользователя, хранит в себе только город\n
        # *connected_to* - указан другой user с которым пользователь общается\n
        # *comment* - комментарий на пользователе, видит только admin\n
        # (нету)*reports* - жалобы на пользователя\n
        # (нету)*bans* - блокировки пользователя\n
        # *log* - log именно этого пользователя

    def toDict(self):
        """
        :return: возвращает объект класса User в виде словаря
        """
        user_dict = {
            "userid": self.userid,
            "name": self.name,
            "age": self.age,
            "sex": self.sex,
            "tags": self.tags,
            # "current_status": self.current_status,
            "location": self.location,
            # "connected_to": self.connected_to,
            "comment": self.comment,
            # "reports": self.reports Пока убираю, переделаю так, чтобы чел был привязан к репортам
            # "bans": self.bans Так же как и с репортами поступаю
            "log": self.log
        }
        return user_dict
