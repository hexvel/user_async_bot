from const import Icons
from vkbottle import VKAPIError
from rules.from_me import IsFromMe
from rules.check_prefix import IsPrefixCommand
from rules.check_command import IsCommand
from vkbottle.user import Message, UserLabeler

blacklist_labeler = UserLabeler()
blacklist_labeler.auto_rules = [
    IsFromMe(),
    IsPrefixCommand(),
    IsCommand(["+чс", "-чс"])
]


@blacklist_labeler.message()
async def blacklist_function(message: Message):
    user_id = message.reply_message.from_id

    if message.text.split()[1].lower() == "+чс":
        try:
            add = await message.ctx_api.account.ban(user_id)
        except VKAPIError[15]:
            text = f"{Icons.YES} [id{user_id}|Уже в черном списке.]"
        finally:
            if add == 1:
                text = f"{Icons.YES} [id{user_id}|Добавлен в черный список.]"
            await message.ctx_api.messages.edit(keep_forward_messages=True, message_id=message.id,
                                                peer_id=message.peer_id, message=text)

    elif message.text.split()[1].lower() == "-чс":
        try:
            delete = await message.ctx_api.account.unban(user_id)
        except VKAPIError[15]:
            text = f"{Icons.NO} [id{user_id}|Пользователь не найден в черном списке.]"
            await message.ctx_api.messages.edit(keep_forward_messages=True, message_id=message.id,
                                                peer_id=message.peer_id, message=text)
        else:
            if delete == 1:
                text = f"{Icons.YES} [id{user_id}|Удален из черного списка.]"

            await message.ctx_api.messages.edit(keep_forward_messages=True, message_id=message.id,
                                                peer_id=message.peer_id, message=text)
