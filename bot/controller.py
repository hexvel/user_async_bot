import asyncio

from bot.command import bot_labelers
from vkbottle.api import API
from vkbottle import BuiltinStateDispenser
from vkbottle.bot import Bot, BotLabeler


class GroupController:
    def __init__(self, token) -> None:
        self.task = None
        self.token = token
        self.session = None

    def init(self):
        api = API(token=self.token)
        bot = BotLabeler()
        for labeler in bot_labelers:
            bot.load(labeler)
        self.session = Bot(
            api=api,
            labeler=bot,
            state_dispenser=BuiltinStateDispenser()
        )

    def start(self):
        self.task = asyncio.create_task(self.session.run_polling())

    def stop(self):
        self.task.cancel()

    def restart(self):
        self.stop()
        self.start()
