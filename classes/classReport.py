class Report:
    def __init__(self, id, user_id, from_user_id, reason: str, comment: str, severity: int):
        """
        :param id: уникальный id report
        :param user_id: Уникальний id пользователя, на которого поступил report
        :param from_user_id: От кого поступил Report
        :param reason: причина репорта
        :param comment: дополнительный комментарий для причины репорта
        :param severity: тяжесть. В зависимости от неё будет приоритет на рассмотрение репорта
        """
        self.id = id
        self.user_id = user_id
        self.from_user_id = from_user_id
        self.comment = comment
        self.reason = reason
        self.severity = severity

    def info(self) -> str:
        """
        Возвараще инофрмацию о репорте в формате str
        """
        return f"Report id: {self.id}\nReason: {self.reason}\nSeverity: {self.severity}"

    def toDict(self) -> dict:
        """
        Создает dict репорта
        :return: dict параметров репорта
        """
        return {
            "id": self.id,
            "userid": self.user_id,
            "from_user_id": self.from_user_id,
            "comment": self.comment,
            "reason": self.reason,
            "severity": self.severity
        }
