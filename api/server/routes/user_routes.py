from fastapi import (
    APIRouter,
    status,
    Depends,
    Body,
    Path,
    HTTPException
)
from fastapi.encoders import jsonable_encoder
from api.server.controller.user_controller import UserController
from api.server.models.response.ResponseModel import ResponseModel
from api.server.models.User import User, UpdateUser
from api.server.models.sub_models.UserInDb import UserInDb
from typing import Any
from api.server.models.params.UserParams import UserQueryParams, GetIDUserQueryParams, UpdateUserQueryParams

router = APIRouter()

controller = UserController()


@router.get('/', response_description='user found all',
            response_model=dict,
            status_code=status.HTTP_200_OK)
async def get_users(query: UserQueryParams = Depends(UserQueryParams)) -> Any:
    users = await controller.find_all_users()
    if users:
        if query.q:
            for user in users:
                user.update({"q": query.q})
        return ResponseModel.success_response(users, "useres data found successfully")
    raise HTTPException(status_code=404, detail="Empty list returned, nothing found")


@router.post('/', response_description='insert user',
             response_model=dict,
             status_code=status.HTTP_201_CREATED)
async def create_user(user: UserInDb = Body(...)) -> Any:
    user = jsonable_encoder(user)
    new_user = await controller.add_user(user)
    return ResponseModel.success_response(new_user, 'Successfully added')


@router.get('/{id}', response_description='find a task',
            response_model=dict,
            status_code=status.HTTP_200_OK)
async def get_task_by_id(query_params: GetIDUserQueryParams = Depends(GetIDUserQueryParams)) -> Any:
    found_task = await controller.find_only_user(query_params.id)
    if found_task:
        return ResponseModel.success_response(found_task, 'Successfully found')
    raise HTTPException(status_code=404, detail="id or data not found")


@router.put('/{id}', response_description='update a task',
            response_model=dict,
            status_code=status.HTTP_200_OK)
async def update_task_by_id(id: str = Path(title="The ID of the item to get"), task: UpdateUser = Body(...)) -> Any:
    request = {k: v for k, v in dict(task).items() if v is not None}
    updated_task = await controller.update_user(id, jsonable_encoder(request))
    if updated_task:
        return ResponseModel.updated_message(id)
    raise HTTPException(status_code=404, detail="student not found")


@router.delete('/{id}', response_description='delete a task',
               response_model=dict,
               status_code=status.HTTP_200_OK)
async def destroy_task_by_id(query_params: GetIDUserQueryParams = Depends(GetIDUserQueryParams)) -> Any:
    deleted_task = await controller.destroy_user(query_params.id)
    if deleted_task:
        return ResponseModel.delete_message(query_params.id)
    raise HTTPException(status_code=404, detail="student not found")


