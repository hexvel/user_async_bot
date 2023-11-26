from vkbottle.user import UserLabeler, Message
from config import Icons, ProjectData
from models.user import Users
from module.rules.is_command import CommandRule

from module.rules.is_prefix import IsPrefix
from utils.methods import APIMethod

user_prefix_commands = UserLabeler()
user_prefix_commands.vbml_ignore_case = True
user_prefix_commands.auto_rules = [IsPrefix(prefix_type="command")]


@user_prefix_commands.message(CommandRule(command=["!команда", "!command"]))
async def change_prefix_command_wrapper(message: Message):
    methods = APIMethod(message)
    message_split = message.text.split(maxsplit=2)

    if len(message_split) <= 2:
        await methods.edit_messages(f"{Icons.WARNING} Укажите префикс.")
        return

    update_prefix = message_split[2]
    await Users.filter(user_id=message.from_id).update(prefix_command=update_prefix)
    ProjectData.USERS[message.from_id].model.prefix_command = update_prefix
    await methods.edit_messages(f"{Icons.YES} Префикс команд успешно обновлён на ['{update_prefix}'].")


@user_prefix_commands.message(CommandRule(command=["!скрипт", "!script"]))
async def change_script_command_wrapper(message: Message):
    methods = APIMethod(message)
    message_split = message.text.split(maxsplit=2)

    if len(message_split) <= 2:
        await methods.edit_messages(f"{Icons.WARNING} Укажите префикс.")
        return

    update_prefix = message_split[2]
    await Users.filter(user_id=message.from_id).update(predix_script=update_prefix)
    ProjectData.USERS[message.from_id].model.predix_script = update_prefix
    await methods.edit_messages(f"{Icons.YES} Префикс скриптов успешно обновлён на ['{update_prefix}'].")


@user_prefix_commands.message(CommandRule(command=["!админ", "!admin"]))
async def change_admin_command_wrapper(message: Message):
    methods = APIMethod(message)
    message_split = message.text.split(maxsplit=2)

    if len(message_split) <= 2:
        await methods.edit_messages(f"{Icons.WARNING} Укажите префикс.")
        return

    update_prefix = message_split[2]
    await Users.filter(user_id=message.from_id).update(prefix_admin=update_prefix)
    ProjectData.USERS[message.from_id].model.prefix_admin = update_prefix
    await methods.edit_messages(f"{Icons.YES} Префикс админа успешно обновлён на ['{update_prefix}'].")
