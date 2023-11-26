import aiohttp
from typing import Literal


class Request:
    def __init__(self):
        self.url = "https://api.pxolly.com/m/database.get"
        self.database_id = "iris"
        self.access_token = "v8x.A.bZ6IajKfGa4Q.znJU27e8aFn2dyKuUinhijUP4m1vV_5dy2qmcxYdl9ZS8xiL48DnFN-9cA9PLQMUTvNTbbV.Tov8c"

    async def get_iris_base(self, user_ids: int | list, allow_fakes: Literal["false", "true"]):

        if isinstance(user_ids, int):
            user_ids = [user_ids]
        user_ids = ",".join(map(str, user_ids))

        async with aiohttp.ClientSession() as session:
            params = dict(
                access_token=self.access_token,
                user_ids=user_ids,
                allow_fakes=allow_fakes,
                database_id=self.database_id
            )

            async with session.get(self.url, params=params) as resp:
                return await resp.json()
