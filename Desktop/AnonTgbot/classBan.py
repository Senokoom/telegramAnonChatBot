from datetime import datetime, timedelta

class ban:
    def __init__(self, id, reason: str, duration: timedelta):
        """
        id - уникальный номер блокировки
        reason - причина блокировки
        duration - длительность блокировки
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
        pass
    def active() -> bool:
        pass