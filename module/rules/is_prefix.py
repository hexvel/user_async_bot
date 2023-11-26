import typing
from vkbottle import ABCRule
from config import ProjectData
from vkbottle.user import Message


class IsPrefix(ABCRule[Message]):
    def __init__(self, prefix_type: typing.Literal["command", "script", "admin"] = "command"):
        self._type = prefix_type

    async def check(self, message: Message):
        if message.text:
            model = ProjectData.USERS[message.from_id].model

            types = {
                "command": model.prefix_command.lower(),
                "script": model.prefix_script.lower(),
                "admin": model.prefix_admin.lower()
            }

            if self._type in types:
                if self._type == "command":
                    return message.text.lower().split()[0].lower() in [types["command"], ".х"]
                if self._type == "script":
                    return message.text.lower().split()[0].lower() in [types["script"], ".с"]
                if self._type == "admin":
                    return message.text.lower().split()[0].lower() in [types["admin"], ".а"]
            else:
                return False
        else:
            return False
