class Report:
    def __init__(self, id, userid, reason: str, severity: int):
        """
        :param id: уникальный id report
        :param userid: Уникальний id пользователя, на которого поступил report
        :param reason: причина репорта
        :param severity: тяжесть. В зависимости от неё будет приоритет на рассмотрение репорта
        """
        self.id = id
        self.userid = userid
        self.reason = reason
        self.severity = severity

    def info(self) -> str:
        """
        Возвараще инофрмацию о репорте в формате str
        """
        return f"Report id: {self.id}\nReason: {self.reason}\nSeverity: {self.severity}"

