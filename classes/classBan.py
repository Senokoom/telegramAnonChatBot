from datetime import datetime, timedelta


class Ban:
    def __init__(self, id, user_id, reason: str, duration: timedelta, date: datetime):
        """

        :param id: уникальный номер блокировки
        :param user_id: уникальный id пользователя, на которого была отправлена блокировка
        :param reason: причина блокировки
        :param date: когда выдали блокировку
        :param duration: На сколько дней выдали бан
        """
        self.id = id
        self.user_id = user_id
        self.reason = reason
        self.date = date
        self.duration = duration
        self.until = date+duration
        """
        Дата, когда будет закончена блокировка
        """
        self.justified = True
        """
        Оправдана ли блокировка
        """

    def info(self) -> str:
        """
        Возвараще инофрмацию о блокировке в формате str
        """
        return (f"Ban id: {self.id}\nReason: {self.reason}\nDuration: {self.duration}\nYou will be unbanned: "
                f"{self.until.strftime('%Y-%m-%d %H:%M:%S')}")

    def is_active(self) -> bool:
        """
        Возвращает True, если блокировка активна, False, если нет
        """
        return datetime.now() > self.until

    def toDict(self):
        """
        Возвращает dict ban
        :return:
        """
        return {
            "id": self.id,
            "userid": self.user_id,
            "reason": self.reason,
            "date": self.date,
            "duration": self.duration
        }