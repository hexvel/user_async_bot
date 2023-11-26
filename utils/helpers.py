from typing import Literal
from config import Icons
from dataclasses import dataclass
from contextlib import suppress

from vkbottle.user import Message
from vkbottle import API, VKAPIError
from vkbottle.http import AiohttpClient


@dataclass
class Helper:
    message: Message = object

    async def token_is_valid(self, token: str) -> bool:  # type: ignore
        ok = False
        api = API(token=token, http_client=AiohttpClient())
        with suppress(VKAPIError):
            apps = await api.apps.get()
            ok = True if apps.items[0].id in [6121396] else False
        await api.http_client.close()
        return ok

    async def get_users(
            self,
            message: Message,
            users: list,
            _type: Literal["['Ignore']", "['Trust']"]
    ) -> str:  # type: ignore
        send_message = ""

        if users:
            send_message += f"{Icons.USERS} Список пользователей в {_type}:"

            for count, user in enumerate(users, 1):
                user_get = await message.ctx_api.users.get(user_ids=user)
                send_message += f"\n{count}. {Icons.USER} [id{user}|{user_get[0].first_name} {user_get[0].last_name}]"
        else:
            send_message += f"{Icons.NO} Список {_type} пуст."

        return send_message
