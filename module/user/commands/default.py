import time
from vkbottle.user import UserLabeler, Message

from config import Icons, ProjectData
from models.user import Users
from utils.methods import APIMethod

from module.rules.is_prefix import IsPrefix
from module.rules.search_user import SearchId
from module.rules.is_command import CommandRule

user_default_commands = UserLabeler()
user_default_commands.vbml_ignore_case = True
user_default_commands.auto_rules = [IsPrefix(prefix_type="command")]


@user_default_commands.message(CommandRule(command=['пинг', 'ping']))
async def ping_user_command_wrapper(message: Message):
    methods = APIMethod(message)
    ping = time.time() - message.date
    await methods.edit_messages(f"{Icons.EARTH} PingTime: {ping:.2f}s.".replace("-", ""))


@user_default_commands.message(CommandRule(command=["!ник", "!nick"]))
async def change_nickname_command_wrapper(message: Message):
    methods = APIMethod(message)
    message_split = message.text.split(maxsplit=2)

    if len(message_split) <= 2:
        await methods.edit_messages(f"{Icons.WARNING} Укажите желаемый никнейм.")
        return

    username = message_split[2]
    await Users.filter(user_id=message.from_id).update(username=username)
    ProjectData.USERS[message.from_id].model.username = username
    await methods.edit_messages(f"{Icons.YES} Никнейм успешно изменён на ['{username}'].")


user_default_commands.auto_rules.append(SearchId())


@user_default_commands.message(CommandRule(command=['+др', '+fr']))
async def add_friend_command_wrapper(message: Message, user_id: int):
    methods = APIMethod(message)
    add_friend = await message.ctx_api.friends.add(user_id=user_id)

    if add_friend == 1:
        message = f"{Icons.USER} [id{user_id}|Пользователю] отправлен запрос на дружбу."
    elif add_friend == 2:
        message = f"{Icons.USER} Заявка [id{user_id}|пользователя] одобрена."
    elif add_friend == 4:
        message = f"{Icons.USER} [id{user_id}|Пользователю] отправлен повторный запрос на дружбу."

    await methods.edit_messages(message)


@user_default_commands.message(CommandRule(command=['-др', '-fr']))
async def delete_friend_command_wrapper(message: Message, user_id: int):
    methods = APIMethod(message)
    delete_friend = await message.ctx_api.friends.delete(user_id=user_id)

    if delete_friend.success == 1:
        message = f"{Icons.USER} [id{user_id}|Пользователь] удалён из друзей."
    elif delete_friend.out_request_deleted == 1:
        message = f"{Icons.USER} Отменяю исходящюю заявку [id{user_id}|пользователю]."
    elif delete_friend.in_request_deleted == 1:
        message = f"{Icons.USER} Отменяю входящюю заявку от [id{user_id}|пользователя]."

    await methods.edit_messages(message)


@user_default_commands.message(CommandRule(command=['+чс', '-bl']))
async def add_black_list(message: Message, user_id: int):
    methods = APIMethod(message)
    add_black_list = await message.ctx_api.account.ban(owner_id=user_id)

    if add_black_list == 1:
        message = f"{Icons.YES} [id{user_id}|Пользователь] заблокирован."
    else:
        message = f"{Icons.NO} Не удалось заблокировать [id{user_id}|пользователя]"

    await methods.edit_messages(message)


@user_default_commands.message(CommandRule(command=['-чс', '-bl']))
async def delete_black_list(message: Message, user_id: int):
    methods = APIMethod(message)
    delete_black_list = await message.ctx_api.account.unban(owner_id=user_id)

    if delete_black_list == 1:
        message = f"{Icons.YES} [id{user_id}|Пользователь] разблокирован."
    else:
        message = f"{Icons.NO} Не удалось разблокировать [id{user_id}|пользователя]"

    await methods.edit_messages(message)


@user_default_commands.message(CommandRule(command=['инфо', 'info']))
async def get_user_info_command_wrapper(message: Message, user_id: int):
    methods = APIMethod(message)

    user = await Users.filter(user_id=user_id).first()

    if not user:
        return await methods.edit_messages(
            f"{Icons.WARNING} [id{user_id}|Пользователь не найден.]"
        )

    is_valid_token = Icons.YES if user.token != "None" else Icons.NO
    profile_photo = user.profile_photo

    rank_status = {
        5: "Владелец", 4: "Главный", 3: "Админ", 2: "Модератор", 1: "Пользователь"
    }

    user_profile = f"{Icons.KING} Информация о [id{user_id}|пользователе]"
    user_profile += f"\n{Icons.MONEY} Баланс пользователя: {user.balance}"
    user_profile += f"\n{Icons.USERS} Состав пользователя: {user.squad}"
    user_profile += f"\n{Icons.CLEVER} Никнейм пользователя: {user.username}"
    user_profile += f"\n{Icons.SI} Ранг пользователя: {rank_status[user.rank]}"
    user_profile += f"\n{Icons.LINK} Токен пользователя: {is_valid_token}"
    user_profile += "\n"
    user_profile += f"\n{Icons.SETTINGS} Префиксы пользователя:"
    user_profile += f"\n{Icons.RIGHT} Префикс команд: {user.prefix_command} | .х"
    user_profile += f"\n{Icons.RIGHT} Префикс скриптов: {user.prefix_script} | .с"
    user_profile += f"\n{Icons.RIGHT} Префикс админа: {user.prefix_admin} | .а"

    await methods.edit_messages(
        user_profile, attachment=profile_photo
    )
