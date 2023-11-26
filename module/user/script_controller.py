import asyncio
import random
import time

from loguru import logger
from vkbottle import API
from lib.cover import CoverImage
from models.user import Scripts


class ScriptController:
    def __init__(self, model: Scripts, api: API):
        self.__task = None
        self.__model = model
        self.__api = api

        self.recommendation = self.__model.recommendation
        self.start_condition_recomendation = 0
        self.stop_condition_recomendation = 0

        self.auto_farm = self.__model.auto_farm
        self.start_condition_auto_farm = 0
        self.stop_condition_auto_farm = 0

        self.auto_status = self.__model.auto_status
        self.start_condition_auto_status = 0
        self.stop_condition_auto_status = 0

        self.auto_cover = self.__model.auto_cover
        self.cover_id = self.__model.cover_id
        self.start_condition_auto_cover = 0
        self.stop_condition_auto_cover = 0

    async def auto_farm_recovery(self):
        await self.__api.messages.send(peer_id=-174105461, message="Ферма", random_id=0)
        start = time.time()
        stop = random.randint(14400, 14405)

        return start, stop

    async def auto_cover_recovery(self):
        data = await Scripts.filter(user_id=self.__model.user_id).first()
        cover = CoverImage(self.__api, data.user_id, data.cover_id)
        cover.draw()
        await cover.upload()

        start = time.time()
        stop = random.randint(60, 65)

        return start, stop

    async def scripts_condition(self):
        response_function = False
        data = await Scripts.filter(user_id=self.__model.user_id).first()

        if self.recommendation and not response_function:
            response_function = True
        self.stop_condition_recomendation = data.recommendation

        if self.auto_farm and not response_function:
            response_function = True
        self.auto_farm = data.auto_farm

        if self.auto_status and not response_function:
            response_function = True
        self.auto_status = data.auto_status

        if self.auto_cover and not response_function:
            response_function = True
        self.auto_cover = data.auto_cover

        return response_function

    async def listen_script_events(self):
        logger.info("Starting listen script events")
        while True:
            if not await self.scripts_condition():
                await asyncio.sleep(20)
            else:
                await asyncio.sleep(10)

            if self.auto_farm:
                if (self.start_condition_auto_farm + self.stop_condition_auto_farm) < time.time():
                    start, stop = await self.auto_farm_recovery()
                    self.start_condition_auto_farm = start
                    self.stop_condition_auto_farm = stop

            if self.auto_cover:
                if (self.start_condition_auto_cover +
                        self.stop_condition_auto_cover) < time.time():
                    start, stop = await self.auto_cover_recovery()
                    self.start_condition_auto_cover = start
                    self.stop_condition_auto_cover = stop

    async def run_script_listen(self):
        self.__task = asyncio.get_event_loop()
        logger.info("Running script listener")
        self.__task.create_task(self.listen_script_events())

    async def stop_script_listen(self):
        self.__task.close()
