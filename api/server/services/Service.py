from abc import ABC, abstractmethod


class Service(ABC):

    def __init__(self):
        pass

    # Find all tasks present in database
    @abstractmethod
    async def find_all(self) -> list[dict]:
        pass

    # Add a new task into the database
    @abstractmethod
    async def add_item(self, item_data: dict) -> dict:
        pass

    # Find one task by id present in database
    @abstractmethod
    async def find_only_item(self, id: str) -> dict:
        pass

    # Update a task with a maching id
    @abstractmethod
    async def update_item(self, id: str, item_data: dict) -> bool:
        pass

    # Delete a task by id present in database
    @abstractmethod
    async def destroy_item(self, id: str) -> bool:
        pass

