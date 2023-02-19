from .Service import Service
from api.server.db import get_collection
from api.server.helpers.parsers.task_parsers import task_parser
from bson.objectid import ObjectId


class TaskService(Service):

    def __init__(self):
        self.collection = get_collection("task")

    # Find all tasks present in database
    async def find_all(self) -> list[dict]:
        return [task_parser(task) async for task in self.collection.find()]

    # Add a new task into the database
    async def add_item(self, task_data: dict) -> dict:
        task = await self.collection.insert_one(task_data)
        new_task = await self.collection.find_one({'_id': task.inserted_id})
        return task_parser(new_task)

    # Find one task by id present in database
    async def find_only_item(self, id: str) -> dict:
        found_task = await self.collection.find_one({'_id': ObjectId(id)})
        return task_parser(found_task)

    # Update a task with a maching id
    async def update_item(self, id: str, task_data: dict) -> bool:
        if len(task_data) < 1:
            return False
        found_task = await self.collection.find_one({'_id': ObjectId(id)})
        if found_task:
            updated_task = await self.collection.update_one({"_id": ObjectId(id)}, {'$set': task_data})
            if updated_task:
                return True
            return False

    # Delete a task by id present in database
    async def destroy_item(self, id: str) -> bool:
        found_task = self.collection.find_one({'_id': ObjectId(id)})
        if found_task:
            await self.collection.delete_one({"_id": ObjectId(id)})
            return True
        return False

