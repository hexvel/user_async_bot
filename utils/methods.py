from vkbottle.user import Message
from dataclasses import dataclass


@dataclass
class APIMethod:
    message: Message = object
    success: bool = False
    data: dict = dict

    async def edit_messages(
        self,
        text: str = None,
        message_id: int = None,
        attachment: str = None
    ) -> None:
        """Edit message.

        Returns:
            NoneType: None
        """

        if message_id is None:
            message_id = self.message.id

        try:
            await self.message.ctx_api.messages.edit(
                peer_id=self.message.peer_id,
                message_id=message_id,
                keep_forward_messages=True,
                message=text,
                attachment=attachment
            )

            self.success = True
            self.data = text
        except Exception as error:
            self.success = False
            self.data = error

    async def send_messages(self, text: str) -> None:
        """Send message.

        Returns:
            NoneType: None
        """

        try:
            await self.message.ctx_api.messages.send(
                peer_id=self.message.peer_id,
                message=text,
                random_id=0
            )

            self.success = True
            self.data = text
        except Exception as error:
            self.success = False
            self.data = error
