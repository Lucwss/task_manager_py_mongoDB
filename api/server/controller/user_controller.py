from api.server.services.UserService import UserService

user_service = UserService()


class UserController:

    def __init__(self):
        pass

    # Find all tasks present in database
    async def find_all_users(self) -> list[dict]:
        return await user_service.find_all()

    # Add a new task into the database
    async def add_user(self, user_data: dict) -> dict:
        return await user_service.add_item(user_data)

    # Find one task by id present in database
    async def find_only_user(self, id: str) -> dict:
        return await user_service.find_only_item(id)

    # Find one task by name present in database
    async def find_only_user_by_name(self, name: str) -> dict:
        return await user_service.find_only_item_by_name(name)

    # Update a task with a maching id
    async def update_user(self, id: str, user_data: dict) -> bool:
        return await user_service.update_item(id, user_data)

    # Delete a task by id present in database
    async def destroy_user(self, id: str) -> bool:
        return await user_service.destroy_item(id)

