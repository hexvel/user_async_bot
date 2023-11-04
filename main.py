import uvicorn
import loguru

from const import Icons

from fastapi import FastAPI
from tortoise import Tortoise
from models.users import Users

from user.controller import UserController
from bot.controller import GroupController
from config import TORTOISE_ORM, ProjectVariables, ProjectData

app = FastAPI()
loguru.logger.disable('vkbottle')


@app.on_event('startup')
async def startup_tortoise():
    await Tortoise.init(TORTOISE_ORM)
    await Tortoise.generate_schemas()


@app.on_event('startup')
async def start_user():
    users = await Users.all()
    for user in users:
        ProjectVariables.USERS[user.user_id] = UserController(user)
        ProjectVariables.USERS[user.user_id].init()
        ProjectVariables.USERS[user.user_id].start()


@app.on_event('startup')
async def start_bot():
    bot = GroupController(ProjectData.GROUP_TOKEN)
    bot.init()
    bot.start()


@app.on_event('shutdown')
async def shutdown():
    await Tortoise.close_connections()


@app.get("/api/user/create")
async def create_user(
    token: str,
    user_id: int
):
    if await Users.filter(user_id=user_id).first() is not None:
        await Users.filter(user_id=user_id).update(token=token)
        user = await Users.filter(user_id=user_id).first()
        ProjectVariables.USERS[user_id] = UserController(user)
        ProjectVariables.USERS[user_id].run()
        text = {"status": "ok",
                "message": f"{Icons.YES} user token updated", "user_id": user_id}
    else:
        await Users.create(user_id=user_id, token=token)
        user = await Users.filter(user_id=user_id).first()
        ProjectVariables.USERS[user_id] = UserController(user)
        ProjectVariables.USERS[user_id].run()
        text = {"status": "ok",
                "message": f"{Icons.YES} user created", "user_id": user_id}
    return text


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=80)
