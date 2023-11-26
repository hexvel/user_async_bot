from vkbottle import ABCRule
from config import ProjectData
from vkbottle.user import Message


class FromMe(ABCRule[Message]):
    async def check(self, message: Message):
        return bool(message.out)
