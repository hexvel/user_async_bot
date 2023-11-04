from user.command.ping_command import ping_labeler
from user.command.friend_commands import friend_labeler
from user.command.blacklist_commands import blacklist_labeler
from user.command.delete_messages import delete_messages_labeler
from user.command.gpt_commands import user_gpt_labeler
from user.command.user_info import user_info_labeler

__all__ = (
    "ping_labeler",
    "friend_labeler",
    "blacklist_labeler",
    "delete_messages_labeler",
    "user_info_labeler",
    "user_gpt_labeler"
)

user_labelers = [
    ping_labeler,
    friend_labeler,
    blacklist_labeler,
    delete_messages_labeler,
    user_info_labeler,
    user_gpt_labeler
]
