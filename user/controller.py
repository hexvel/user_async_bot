import asyncio

from user.command import user_labelers
from vkbottle.api import API
from vkbottle import BuiltinStateDispenser
from vkbottle.user import User, UserLabeler


class DataUser:
    def __init__(self, user):
        self.prefix_commands = [".х", user.prefix_commands]
        self.scripts_prefix = [".с", user.prefix_scripts]
        self.admin_prefix = [".а", user.prefix_admin]
        self.gpt_prefix = [".гпт", "/gpt", ".gpt"]


class UserController:
    def __init__(self, user) -> None:
        self.task = None
        self.user = user
        self.session = None
        self.data = DataUser(self.user)

    def init(self):
        api = API(token=self.user.token)
        user = UserLabeler()
        for labeler in user_labelers:
            user.load(labeler)
        self.session = User(
            api=api,
            labeler=user,
            state_dispenser=BuiltinStateDispenser()
        )

    def start(self):
        self.task = asyncio.create_task(self.session.run_polling())

    def stop(self):
        self.task.cancel()

    def restart(self):
        self.stop()
        self.start()

    def run(self):
        self.init()
        self.start()
