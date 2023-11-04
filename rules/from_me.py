from vkbottle import ABCRule
from config import ProjectVariables
from vkbottle.user import Message


class IsFromMe(ABCRule):
    async def check(self, message: Message):
        return message.out == 1
