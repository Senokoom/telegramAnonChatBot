class Report:
    def __init__(self, id: str, reason: str, severity: int):
        """

        :param id: уникальный id report
        :param reason: причина репорта
        :param severity: тяжесть. В зависимости от неё будет приоритет на рассмотрение репорта
        """
        self.id = id
        self.reason = reason
        self.severity = severity

    def info(self) -> str:
        """
        Возвараще инофрмацию о репорте в формате str
        """
        return f"Ban id: {self.id}\nReason: {self.reason}\nSeverity: {self.severity}"

