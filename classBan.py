from datetime import datetime, timedelta

class ban:
    def __init__(self, id, reason: str, duration: timedelta):
        """

        :param id: уникальный номер блокировки
        :param reason: причина блокировки
        :param duration: длительность блокировки
        """
        self.id = id
        self.reason = reason
        self.duration = duration
        self.until = datetime.now() + duration
        """
        Дата, когда будет закончена блокировка
        """
        self.justified = True
        """
        Оправдана ли блокировка
        """

    def info(self):
        """
        Возвараще инофрмацию о блокировке в формате str
        """
        return f"Ban id: {self.id}\nReason: {self.reason}\nDuration: {self.duration}\nYou will be unbanned: {self.until.strftime("%Y-%m-%d %H:%M:%S")}"

    def is_active(self) -> bool:
        """
        Возвращает True, если блокировка активна, False, если нет
        """
        return datetime.now() > self.until
