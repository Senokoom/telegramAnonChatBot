from aiogram import Bot, Dispatcher, F, Router
import asyncio
import os
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

class TelegramBot:



    def __init__(self):
        load_dotenv()
        token = os.getenv("TELEGRAM_TOKEN")
        self.router = Router()
        self.bot = Bot(token=token)
        self.dp = Dispatcher()
        self.dp.include_router(router=self.router)
        self._register_handlers()


    def _register_handlers(self):
        self.router.message.register(self.start_cmd, CommandStart())
        self.router.message.register(self.echo_text, F.text)
        


    async def send_str_message(self, user_id, message_text: str):
        await self.bot.send_message(user_id, text=message_text)


    async def start_cmd(self, message):
        await message.answer("Дарова пидр")

    async def echo_text(self, message):
        await message.answer(message.text)

    async def start_bot(self):
        await self.dp.start_polling(self.bot)


t = TelegramBot()
asyncio.run(t.start_bot())