from fastapi import (
    APIRouter,
    status,
    Depends,
    Body,
    Path,
    HTTPException
)
from fastapi.encoders import jsonable_encoder
from api.server.controller.task_controller import TaskController
from api.server.models.response.ResponseModel import ResponseModel
from api.server.models.Task import Task, UpdateTask
from typing import Any
from api.server.models.params.TaskParams import TaskQueryParams, GetIDTaskQueryParams, UpdateTaskQueryParams

router = APIRouter()

controller = TaskController()


@router.get('/', response_description='task found all',
            response_model=dict,
            status_code=status.HTTP_200_OK)
async def get_tasks(query: TaskQueryParams = Depends(TaskQueryParams)) -> Any:
    tasks = await controller.find_all_tasks()
    if tasks:
        if query.q:
            for task in tasks:
                task.update({"q": query.q})
        return ResponseModel.success_response(tasks, "tasks data found successfully")
    raise HTTPException(status_code=404, detail="Empty list returned, nothing found")


@router.post('/', response_description='insert task',
             response_model=dict,
             status_code=status.HTTP_201_CREATED)
async def create_task(task: Task = Body(...)) -> Any:
    task = jsonable_encoder(task)
    new_task = await controller.add_task(task)
    return ResponseModel.success_response(new_task, 'Successfully added')


@router.get('/{id}', response_description='find a task',
            response_model=dict,
            status_code=status.HTTP_200_OK)
async def get_task_by_id(query_params: GetIDTaskQueryParams = Depends(GetIDTaskQueryParams)) -> Any:
    found_task = await controller.find_only_task(query_params.id)
    if found_task:
        return ResponseModel.success_response(found_task, 'Successfully found')
    raise HTTPException(status_code=404, detail="id or data not found")


@router.put('/{id}', response_description='update a task',
            response_model=dict,
            status_code=status.HTTP_200_OK)
async def update_task_by_id(id: str = Path(title="The ID of the item to get"), task: UpdateTask = Body(...)) -> Any:
    request = {k: v for k, v in dict(task).items() if v is not None}
    updated_task = await controller.update_task(id, jsonable_encoder(request))
    if updated_task:
        return ResponseModel.updated_message(id)
    raise HTTPException(status_code=404, detail="student not found")


@router.delete('/{id}', response_description='delete a task',
               response_model=dict,
               status_code=status.HTTP_200_OK)
async def destroy_task_by_id(query_params: GetIDTaskQueryParams = Depends(GetIDTaskQueryParams)) -> Any:
    deleted_task = await controller.destroy_task(query_params.id)
    if deleted_task:
        return ResponseModel.delete_message(query_params.id)
    raise HTTPException(status_code=404, detail="student not found")


