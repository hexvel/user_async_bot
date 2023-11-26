from typing import Union
from vkbottle import ABCRule
from vkbottle.user import Message


class CommandRule(ABCRule):
    def __init__(self, command: Union[str, list[str]] = None):
        self.command = command

    async def check(self, message: Message):
        if message.text:
            if len(message.text.split()) > 1:
                return message.text.lower().split()[1] in self.command
