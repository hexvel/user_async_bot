from vkbottle.user import UserLabeler


class ProjectData:
    BASE_MODEL = "models.users"
    GPT_TOKEN = "API"
    GROUP_TOKEN = "TOKEN"
    BASE_PATH = "mysql://user:password@ip:3306/databas"


class ProjectVariables:
    USERS = {}


TORTOISE_ORM = {
    "connections": {"default": ProjectData.BASE_PATH},
    "apps": {
        "models": {
            "models": ["models.users", "models.website", "aerich.models"],
            "default_connection": "default",
        }
    }
}
