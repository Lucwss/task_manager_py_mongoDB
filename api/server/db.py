import motor.motor_asyncio
from dotenv import find_dotenv, load_dotenv
import asyncio
import os
from api.server.helpers.parsers.task_parsers import task_parser

load_dotenv(find_dotenv())


client = motor.motor_asyncio.AsyncIOMotorClient(os.environ.get('MONGO_URL_LOCAL'))
db_localDB = client['localDB']


async def create_new_collection(name: str):
    try:
        await db_localDB.create_collection(name)
    except Exception as ep:
        print(f"Error: {ep}")


def get_collection(name: str):
    try:
        collection = db_localDB.get_collection(name)
        return collection
    except Exception as ep:
        print(f"Error trying to get collections: {ep}")


async def create_data():
    tasks = [
        {
            "name": "wash the dishes",
            "status": False,
            "description": "you need to wash all of your dishes until 6:34 pm"
        },
        {
            "name": "study for the course",
            "status": False,
            "description": "you need to study for the course until 6:34 pm"
        },
        {
            "name": "pray to your God father",
            "status": False,
            "description": "you need to do it until 6:34 pm"
        }
    ]

    task_collection = db_localDB.task
    await asyncio.sleep(1)
    ids = await task_collection.insert_many(tasks)
    await asyncio.sleep(1)
    aux = [task_parser(item) async for item in task_collection.find()]
    await asyncio.sleep(1)
    data = ids.inserted_ids
    await asyncio.sleep(1)

    users = [
        {
            "user_name": "teste_one",
            "email": "teste_one@example.com",
            "tasks": aux,
            "birthdate": "2012-03-11 00:00:00",
            "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
            "disabled": False
        },
    ]

    user_collection = db_localDB.user
    await user_collection.insert_many(users)
if __name__ == "__main__":
    loop = client.get_io_loop()
    loop.run_until_complete(create_data())
