from vkbottle import ABCRule
from config import ProjectVariables
from vkbottle.user import Message


class IsPrefixCommand(ABCRule[Message]):
    async def check(self, message: Message):
        prefixes = ProjectVariables.USERS[message.from_id].data.prefix_commands
        return message.text.lower().split()[0] in prefixes


class IsPrefixScript(ABCRule[Message]):
    async def check(self, message: Message):
        prefixes = ProjectVariables.USERS[message.from_id].data.scripts_prefix
        return message.text.lower().split()[0] in prefixes


class IsPrefixAdmin(ABCRule[Message]):
    async def check(self, message: Message):
        prefixes = ProjectVariables.USERS[message.from_id].data.admin_prefix
        return message.text.lower().split()[0] in prefixes


class IsPrefixGPT(ABCRule[Message]):
    async def check(self, message: Message):
        prefixes = ProjectVariables.USERS[message.from_id].data.gpt_prefix
        return message.text.lower().split()[0] in prefixes
