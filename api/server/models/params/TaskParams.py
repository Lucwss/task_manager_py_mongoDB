from fastapi import (
    Query,
    Path,
    Body
)
from api.server.models.Task import UpdateTask


class TaskQueryParams:
    def __init__(self, q: str | None = Query(default=None, title='query string', alias='q', max_length=10, min_length=3)):
        self.q = q


class GetIDTaskQueryParams:
    def __init__(self, id: str = Path(title="The ID of the item to get")):
        self.id = id


class UpdateTaskQueryParams:
    def __init__(self, id: str = Path(title="The ID of the item to get"), task: UpdateTask = Body(...)):
        self.id = id
        self.task = task
