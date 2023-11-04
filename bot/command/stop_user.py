from const import Icons
from config import ProjectVariables
from models.users import Users
from vkbottle.dispatch.rules.base import CommandRule
from vkbottle.bot import BotLabeler, Message

bot_stop_user_labeler = BotLabeler()


@bot_stop_user_labeler.message(CommandRule("стоп", ['.', '!', '/']))
async def stop_user_bot(message: Message):
    user_exist = await Users.filter(user_id=message.from_id).first()

    if user_exist is None:
        text = f"{Icons.WARNING} Вы не зарегистрированы в модуле."
        await message.answer(text)
        return

    ProjectVariables.USERS[message.from_id].stop()
    text = f"{Icons.YES} Модуль успешно остановлен."
    await message.answer(text)
