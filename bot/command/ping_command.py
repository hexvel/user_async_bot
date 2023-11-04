import time

from const import Icons
from vkbottle.dispatch.rules.base import CommandRule
from vkbottle.bot import BotLabeler, Message

bot_ping_labeler = BotLabeler()


@bot_ping_labeler.message(CommandRule("пинг", ['.', '!', '/']))
async def ping_bot(message: Message):
    ping = time.time() - message.date
    text = f"{Icons.EARTH} PingTime: {ping:.3f}s."

    await message.answer(text)
