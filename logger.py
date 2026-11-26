import logging
from pathlib import Path
from logging.handlers import RotatingFileHandler


class Log:
    def __init__(self, log_target: str, log_dir: str):
        self.logger = self.setup_logger(log_target, log_dir)



    def setup_logger(self, log_target: str, log_dir):
        # Создаем логгер

        logger = logging.getLogger(log_target)
        if logger.handlers:
            return logger

        logger.setLevel(logging.DEBUG) # Ловим всё, от отладки до критических ошибок
        # Формат сообщений: [ВРЕМЯ] УРОВЕНЬ: Сообщение
        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)-8s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        log_path = Path(log_dir)
        ("logs" / log_path).mkdir(parents=True, exist_ok=True)
        file_path = "logs" / log_path / f"{log_target}.log"

        # 1. Обработчик для консоли (выводит INFO и выше)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)

        # 2. Обработчик для файла (сохраняет всё, включая DEBUG)
        # Файл будет создаваться в папке с проектом

        file_handler = RotatingFileHandler(
            file_path, maxBytes=5 * 1024 * 1024, backupCount=3, encoding="utf-8"
        )

        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        # Добавляем обработчики к логгеру (проверяем, чтобы не дублировать при повторном импорте)
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        return logger