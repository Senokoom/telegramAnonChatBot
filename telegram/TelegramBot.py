from logging import Logger

from aiogram import Bot, Dispatcher, F, Router
import asyncio
import os

from aiogram.filters.command import Command
from aiogram.exceptions import AiogramError
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv
from logger import Log
from managers.UserManager import UserManager


class TelegramBot:
    def __init__(self):
        self.log = Log("telegram", "telegram").logger
        self.log.info("---------------------------------------------NEW SESSION----------------------------------------------------")
        load_dotenv()
        token = os.getenv("TELEGRAM_TOKEN")
        try:
            self.router = Router()
            self.bot = Bot(token=token)
            self.dp = Dispatcher()
            self.dp.include_router(router=self.router)
            self._register_handlers()
            self.user_manager = UserManager()
            self.log.info("Бот ТГ успешно запущен")
        except AiogramError as e:
            self.log.error(f"Бот обрушился с ошибкой {e}")


    def _register_handlers(self):
        self.log.info("Регестрирую handlers")
        self.router.message.register(self.start_cmd, CommandStart())
        self.router.message.register(self.setup_user_profile, Command('setup'))
        self.router.message.register(self.echo_text, F.text)


    async def setup_user_profile(self, message):
        await message.answer("setup acc")


    async def send_str_message(self, user_id, message_text: str):
        await self.bot.send_message(user_id, text=message_text)


    async def start_cmd(self, message: Message):
        """
        Реакция на /start
        """
        self.log.info("Получил команду /start")
        #Из этого состоит message.from_user
        '''
        id=994917029
         is_bot=False
          first_name='Лев'
           last_name='Кочин'
            username='levkoch1n'
             language_code='ru'
              is_premium=None
               added_to_attachment_menu=None
                can_join_groups=None
                 can_read_all_group_messages=None
                  supports_guest_queries=None
                   supports_inline_queries=None
                    can_connect_to_business=None
                     has_main_web_app=None
                      has_topics_enabled=None
                       allows_users_to_create_topics=None
                        can_manage_bots=None
                         supports_join_request_queries=None
        '''
        response = self.user_manager.get_user_by_id(str(message.from_user.id))
        if response:
            self.log.info("User найден в нашей базе")
            await self.send_str_message(message.from_user.id,f"User is found: {response}\nId: {message.from_user.id}")
        else:
            self.log.info("User НЕ найден в нашей базе, сохраняю нового User в память")
            msg_user = message.from_user
            self.user_manager.create_and_save_user({
                "id": str(message.from_user.id),
                "name": f"{msg_user.first_name or ''} {msg_user.last_name or ''}".strip() or msg_user.username or "",
                "age": 0,
                "sex": ''
            })

    async def echo_text(self, message):
        await message.answer(message.text)

    async def start_bot(self):
        await self.dp.start_polling(self.bot)