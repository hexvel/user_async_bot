import re
from vkbottle.user import rules,  Message


class SearchId(rules.ABCRule[Message]):
    async def check(self, event: Message):
        message = event.text
        data = dict()

        if event.reply_message:
            data["user_id"] = event.reply_message.from_id

        elif len(message.split(maxsplit=2)) < 3:
            data["user_id"] = event.from_id
        else:
            data["user_id"] = re.findall(r"\d+", message)[0]

        return data
