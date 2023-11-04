import openai

from const import Icons
from config import ProjectData
from rules.from_me import IsFromMe
from rules.check_prefix import IsPrefixGPT
from rules.check_command import IsCommand
from vkbottle.user import Message, UserLabeler

user_gpt_labeler = UserLabeler()
user_gpt_labeler.auto_rules = [
    IsFromMe(),
    IsPrefixGPT()
]


@user_gpt_labeler.message()
async def gpt_function(message: Message):
    if len(message.text.split(maxsplit=1)) < 2:
        await message.ctx_api.messages.edit(
            keep_forward_messages=True,
            peer_id=message.peer_id,
            message=f"{Icons.WARNING} Напишите текст запроса.",
            message_id=message.id,
        )
        return

    await message.ctx_api.messages.edit(
        keep_forward_messages=True,
        peer_id=message.peer_id,
        message=f"{Icons.LOADING} Обработка запроса.",
        message_id=message.id,
    )

    openai.api_key = ProjectData.GPT_TOKEN
    completion = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message.text.split(maxsplit=1)[
            1]}]
    )

    await message.ctx_api.messages.edit(
        keep_forward_messages=True,
        peer_id=message.peer_id,
        message=completion['choices'][0]['message']['content'],
        message_id=message.id,
    )
