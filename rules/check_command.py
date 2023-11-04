from typing import Union
from vkbottle import ABCRule
from vkbottle.user import Message


class IsCommand(ABCRule):
    def __init__(self, command: Union[str, list[str]] = None):
        self.command = command

    async def check(self, message: Message):
        return message.text.lower().split()[1] in self.command
