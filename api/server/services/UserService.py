from .Service import Service
from api.server.db import get_collection
from api.server.helpers.parsers.user_parsers import user_parser
from bson.objectid import ObjectId
from .TaskService import TaskService
from api.server.helpers.auth.hash_method import get_password_hash
task_service = TaskService()


class UserService(Service):

    def __init__(self):
        self.collection = get_collection("user")
        self.collection_task = get_collection("task")

    # Find all tasks present in database
    async def find_all(self) -> list[dict]:
        return [user_parser(user) async for user in self.collection.find()]

    # Add a new task into the database
    async def add_item(self, user_data: dict) -> dict:
        tasks = user_data['tasks']
        retrieved_tasks = []

        if tasks is not None:
            for task_id in tasks:
                found = await task_service.find_only_item(task_id)
                retrieved_tasks.append(found)

            user_data['tasks'] = retrieved_tasks
        user_data['hashed_password'] = get_password_hash(user_data['hashed_password'])
        user = await self.collection.insert_one(user_data)
        new_user = await self.collection.find_one({'_id': user.inserted_id})
        return user_parser(new_user)

    # Find one task by id present in database
    async def find_only_item(self, id: str) -> dict:
        found_user = await self.collection.find_one({'_id': ObjectId(id)})
        return user_parser(found_user)

    # Find one task by id present in database
    async def find_only_item_by_name(self, name: str) -> dict:
        found_user = await self.collection.find_one({'user_name': name})
        return user_parser(found_user)

    # Update a task with a maching id
    async def update_item(self, id: str, user_data: dict) -> bool:
        tasks = user_data['tasks']
        retrieved_tasks = []

        if tasks is not None:
            for task_id in tasks:
                found = await task_service.find_only_item(task_id)
                retrieved_tasks.append(found)

            user_data['tasks'] = retrieved_tasks
        if len(user_data) < 1:
            return False
        found_user = await self.collection.find_one({'_id': ObjectId(id)})
        if found_user:
            updated_user = await self.collection.update_one({"_id": ObjectId(id)}, {'$set': user_data})
            if updated_user:
                return True
            return False

    # Delete a task by id present in database
    async def destroy_item(self, id: str) -> bool:
        found_user = self.collection.find_one({'_id': ObjectId(id)})
        if found_user:
            await self.collection.delete_one({"_id": ObjectId(id)})
            return True
        return False