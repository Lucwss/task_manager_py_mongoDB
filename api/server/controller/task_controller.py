from api.server.db import get_collection
from api.server.services.TaskService import TaskService

task_service = TaskService()


class TaskController:

    def __init__(self):
        pass

    # Find all tasks present in database
    async def find_all_tasks(self) -> list[dict]:
        return await task_service.find_all()

    # Add a new task into the database
    async def add_task(self, task_data: dict) -> dict:
        return await task_service.add_item(task_data)

    # Find one task by id present in database
    async def find_only_task(self, id: str) -> dict:
        return await task_service.find_only_item(id)

    # Update a task with a maching id
    async def update_task(self, id: str, task_data: dict) -> bool:
        return await task_service.update_item(id, task_data)

    # Delete a task by id present in database
    async def destroy_task(self, id: str) -> bool:
        return await task_service.destroy_item(id)

