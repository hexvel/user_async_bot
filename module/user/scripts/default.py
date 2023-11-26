from vkbottle.user import Message, UserLabeler
from config import Icons
from models.user import Scripts
from module.rules.is_command import CommandRule

from module.rules.is_prefix import IsPrefix
from utils.methods import APIMethod


user_default_scripts = UserLabeler()
user_default_scripts.vbml_ignore_case = True
user_default_scripts.auto_rules = [IsPrefix(prefix_type="script")]


@user_default_scripts.message(CommandRule(command=['обложка', 'cover']))
async def change_cover_script_wrapper(message: Message):
    methods = APIMethod(message)
    message_split = message.text.split(maxsplit=2)

    if len(message_split) <= 2:
        await methods.edit_messages(f"{Icons.WARNING} Укажите тему обложки.")
        return

    update_theme = message_split[2]
    if update_theme.isdigit():
        await Scripts.filter(user_id=message.from_id).update(cover_id=update_theme)
        await methods.edit_messages(f"{Icons.YES} Тема обложки обновлена на ['{update_theme}'].")
    else:
        await methods.edit_messages(f"{Icons.NO} Укажите тему в виде индексации.")
