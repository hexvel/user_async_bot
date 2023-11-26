import time
from vkbottle.bot import BotLabeler, Message
from vkbottle.dispatch.rules.base import CommandRule

from config import Icons

group_default_commands = BotLabeler()
group_default_commands.vbml_ignore_case = True


@group_default_commands.message(CommandRule("пинг"))
async def ping_group_command_wrapper(message: Message):
    ping = time.time() - message.date
    await message.answer(
        f"{Icons.EARTH} PingTime: {ping:.2f}s.".replace("-", "")
    )
