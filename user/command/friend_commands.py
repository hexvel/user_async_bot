from const import Icons
from vkbottle import VKAPIError
from rules.from_me import IsFromMe
from rules.check_prefix import IsPrefixCommand
from rules.check_command import IsCommand
from vkbottle.user import Message, UserLabeler

friend_labeler = UserLabeler()
friend_labeler.auto_rules = [
    IsFromMe(),
    IsPrefixCommand(),
    IsCommand(["+др", "-др"])
]


@friend_labeler.message()
async def friends_action(message: Message):
    user_id = message.reply_message.from_id

    if message.text.split()[1].lower() == "+др":
        add = await message.ctx_api.friends.add(user_id)
        if add == 2:
            text = f"{Icons.YES} [id{user_id}|Заявка одобрена.]"
        elif add == 1:
            text = f"{Icons.YES} [id{user_id}|Заявка отправлена.]"
        else:
            text = f"{Icons.YES} [id{user_id}|Уже в списке друзей.]"

        await message.ctx_api.messages.edit(keep_forward_messages=True,  message_id=message.id,
                                            peer_id=message.peer_id, message=text)

    elif message.text.split()[1].lower() == "-др":
        try:
            delete = await message.ctx_api.friends.delete(user_id)
        except VKAPIError[15]:
            text = f"{Icons.NO} [id{user_id}|Пользователь не найден в списке друзей.]"
            await message.ctx_api.messages.edit(keep_forward_messages=True, message_id=message.id,
                                                peer_id=message.peer_id, message=text)
        else:
            if delete.success == 1:
                text = f"{Icons.YES} [id{user_id}|Удален из друзей.]"
            elif delete.out_request_deleted == 1:
                text = f"{Icons.YES} [id{user_id}|Исходящая заявка отменена.]"
            elif delete.in_request_deleted == 1:
                text = f"{Icons.YES} [id{user_id}|Входящая заявка отменена.]"

            await message.ctx_api.messages.edit(keep_forward_messages=True, message_id=message.id,
                                                peer_id=message.peer_id, message=text)
