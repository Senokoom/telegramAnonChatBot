import classReport, classBan
from geopy.geocoders import Nominatim
# noinspection SpellCheckingInspection
class User:
    def __init__(self, tgid, name, age, sex, tags: list,
                 current_status, location: dict = None, is_admin: bool = False):
        """
        **Создает нового пользователя**\n
        *tgid* - id Telegram пользователя **(неизменяемое)** \n
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
        self.connected_to: User = None
        self.comment: str = ''
        self.is_admin = is_admin
        self.reports: list[classReport.report] = None
        self.bans: list[classBan.ban] = None
        self.log: list = None

    def info(self):
        """
        Выводит в консоль **данные** (*tgid, name, age, sex, current_status, comment, reports, bans*) пользователя
        """
        print(f"Tgid: {self.tgid}\n"
              f"Name: {self.name}\n"
              f"Age: {self.age}\n"
              f"Sex: {self.sex}\n"
              f"Current status: {self.current_status}\n"
              f"Comment: {self.comment}\n"
              f"Reports: {[x.info() for x in self.reports] if self.reports else 'Нет репортов'}\n"
              f"Bans: {[x.info for x in self.bans] if self.bans else 'Нет блокировок'}")

    def city_isreal(self, location_inp) -> dict | None:
        """
        Проверяет существование города и возвращает *Dict(существует)* или *None* . Поддерживает русские и английские названия.
        """
        geolocator = Nominatim(user_agent="AnonChatTgBot UnivercityProject (leva.kochin@gmail.com)")
        location = geolocator.geocode(location_inp)
        if location:
            return {"city": location_inp,
                    "lat": location.latitude,
                    "lon": location.longitude}
        else:
            return None

    def setup(self):
        """
                Настройка аккаунта пользователя. Позволяет поменять **Имя, Возраст, Пол, Геолокацию, Теги**

                пока что только через консоль
                """
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
               and not (location_dict := self.city_isreal(location_inp))):
            pass
        self.location = location_dict if location_dict else self.location



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