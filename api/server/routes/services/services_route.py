from fastapi import APIRouter
from api.server.helpers.notification import write_notification
from fastapi import BackgroundTasks

router = APIRouter()


@router.post('/send-notification/{email}')
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="hello world")
    return {"message": "Nofitication sent in the background"}
