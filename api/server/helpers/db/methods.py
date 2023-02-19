from api.server.models.sub_models.UserInDb import UserInDb
from api.server.controller.user_controller import UserController


user_controller = UserController()


async def get_user(username: str):
    user = await user_controller.find_only_user_by_name(username)
    if user:
        return UserInDb(**user)


