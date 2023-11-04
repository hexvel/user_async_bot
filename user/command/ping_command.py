import time

from const import Icons
from rules.from_me import IsFromMe
from rules.check_command import IsCommand
from rules.check_prefix import IsPrefixCommand
from vkbottle.user import UserLabeler, Message

ping_labeler = UserLabeler()
ping_labeler.auto_rules = [
    IsFromMe(),
    IsPrefixCommand(),
    IsCommand(['пинг', 'ping'])
]


@ping_labeler.message()
async def ping_user(message: Message):
    ping = time.time() - message.date
    text = f"{Icons.EARTH} PingTime: {ping:.3f}s.".replace("-", "")

    await message.ctx_api.messages.edit(
        keep_forward_messages=True,
        message_id=message.id,
        peer_id=message.peer_id,
        message=text,
    )
