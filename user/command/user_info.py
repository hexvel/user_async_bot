from const import Icons
from vkbottle import VKAPIError
from models.users import Users
from rules.from_me import IsFromMe
from rules.check_prefix import IsPrefixCommand
from rules.check_command import IsCommand
from vkbottle.user import Message, UserLabeler


user_info_labeler = UserLabeler()
user_info_labeler.auto_rules = [
    IsFromMe(),
    IsPrefixCommand(),
    IsCommand(["инфо", "info"])
]


@user_info_labeler.message()
async def get_user_info(message: Message):
    if message.reply_message:
        user_id = message.reply_message.from_id
    else:
        user_id = message.from_id

    user_info = await Users.filter(user_id=user_id).first()

    if user_info is None:
        return await message.answer("Пользователь не найден")

    role_from_rank = {
        5: "Владелец", 4: "Админ", 3: "Модератор",
        2: "Агент", 1: "Пользователь"
    }

    token = Icons.YES if user_info.token != "None" else Icons.NO

    text = f"""
        ╔⫷| [id{user_id}|Инфо пользователя] {Icons.USER}
        ╠⫸| Никнейм: {user_info.nickname}
        ╠⫸| Роль: {role_from_rank[user_info.rank]}
        ╠⫸| Баланс: {user_info.balance}р.
        ║
        ╠⫸| [VKA: {token}]
        ║
        ╠⫸| [id{user_id}|Инфо префиксов] {Icons.SETTINGS}
        ╠⫸| Команды: {user_info.prefix_commands}
        ╠⫸| Скрипты: {user_info.prefix_scripts}
        ╠⫸| Админ: {user_info.prefix_admin}
        ║
        ╚⫸| {Icons.SETTINGS} <-[HEXVEL v:l]-> {Icons.SETTINGS}
    """

    await message.ctx_api.messages.edit(
        peer_id=message.peer_id,
        message_id=message.id,
        message=text
    )
