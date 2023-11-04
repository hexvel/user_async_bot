from bot.command.ping_command import bot_ping_labeler
from bot.command.start_user import bot_start_user_labeler
from bot.command.restart_user import bot_restart_user_labeler
from bot.command.stop_user import bot_stop_user_labeler

__all__ = (
    "bot_ping_labeler",
    "bot_start_user_labeler",
    "bot_restart_user_labeler",
    "bot_stop_user_labeler"
)

bot_labelers = [
    bot_ping_labeler,
    bot_start_user_labeler,
    bot_restart_user_labeler,
    bot_stop_user_labeler
]
