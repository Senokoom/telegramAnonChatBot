from telegram.TelegramBot import TelegramBot
import asyncio

py_bot = TelegramBot()
asyncio.run(py_bot.start_bot())