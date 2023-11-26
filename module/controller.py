import asyncio
import typing

from loguru import logger
from config import GROUP_TOKEN, ProjectData
from models.user import Scripts
from module.user import ScriptController

from .user import user_labelers
from .group import group_labelers

from dataclasses import dataclass
from vkbottle import BuiltinStateDispenser

from vkbottle.api import API
from vkbottle.bot import Bot, BotLabeler
from vkbottle.user import User, UserLabeler


@dataclass
class ModelInterface:
    user_id: int
    token: str
    prefix_command: str
    prefix_script: str
    prefix_admin: str
    prefix_trust: str


class Controller:
    def __init__(
        self,
        _type: typing.Literal['user', 'group'],
        model: ModelInterface | None = None,
        script_model: Scripts = None,
    ):
        self.__task = asyncio.get_event_loop()
        self.__session = None

        self.type = _type
        self.model = model
        self.script_model = script_model

    async def create_user_task(self):
        api = API(token=self.model.token)
        user = UserLabeler()

        for labeler in user_labelers:
            user.load(labeler)

        self.__session = User(api=api, labeler=user,
                              state_dispenser=BuiltinStateDispenser())
        ProjectData.SCRIPTS[self.model.user_id] = ScriptController(
            self.script_model, api)

    async def create_group_task(self):
        api = API(token=GROUP_TOKEN)
        group = BotLabeler()

        for labeler in group_labelers:
            group.load(labeler)

        self.__session = Bot(api=api, labeler=group,
                             state_dispenser=BuiltinStateDispenser())

    async def run_session(self):
        if self.type == "user":
            await self.create_user_task()
            logger.info("Session created successfully for user %s" %
                        self.model.user_id)

        elif self.type == "group":
            await self.create_group_task()
            logger.info("Session created successfully for group")

        self.__task.create_task(self.__session.run_polling())
