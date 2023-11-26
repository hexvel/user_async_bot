import uvicorn

from loguru import logger
from tortoise import Tortoise
from fastapi import FastAPI

from models import Users
from config import ProjectData, tortoise_orm
from models.user import Scripts
from module.controller import Controller

logger.disable("vkbottle")


async def lifespan(app: FastAPI):
    await Tortoise.init(tortoise_orm)
    await Tortoise.generate_schemas()
    logger.info(
        "Finished initialization of tortoise with schema ['tortoise_orm']")

    users = await Users.all()
    for user in users:
        script_model = await Scripts.filter(user_id=user.user_id).first()
        ProjectData.USERS[user.user_id] = Controller(
            "user", user, script_model)
        await ProjectData.USERS[user.user_id].run_session()
        await ProjectData.SCRIPTS[user.user_id].run_script_listen()

    controller = Controller("group")
    await controller.run_session()

    yield
    await Tortoise.close_connections()
    logger.warning("Finished closing connections")

app = FastAPI(lifespan=lifespan)

if __name__ == '__main__':
    uvicorn.run(app=app, host="127.0.0.1", port=5174, log_level="error")
