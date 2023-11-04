from const import Icons
from vkbottle import VKAPIError
from rules.from_me import IsFromMe
from rules.check_prefix import IsPrefixCommand
from rules.check_command import IsCommand
from vkbottle.user import Message, UserLabeler

delete_messages_labeler = UserLabeler()
delete_messages_labeler.auto_rules = [
    IsFromMe(),
    IsPrefixCommand(),
    IsCommand(["дд", "dd"])
]


@delete_messages_labeler.message()
async def user_delete_messages(message: Message):
    count = 2
    del_count = 0
    message_ids = []

    if len(message.text.split()) > 2:
        count = int(message.text.split()[2])+1

    history = await message.ctx_api.messages.get_history(
        peer_id=message.peer_id)

    for item in history.items:
        if del_count >= count: break
        if item.from_id == message.from_id:
            message_ids.append(item.id)
            del_count += 1

    await message.ctx_api.messages.delete(message_ids=message_ids, delete_for_all=1)
