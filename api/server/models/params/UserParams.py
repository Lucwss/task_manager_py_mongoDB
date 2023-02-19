from fastapi import (
    Query,
    Path,
    Body
)
from api.server.models.User import UpdateUser


class UserQueryParams:
    def __init__(self, q: str | None = Query(default=None, title='query string', alias='q', max_length=10, min_length=3)):
        self.q = q


class GetIDUserQueryParams:
    def __init__(self, id: str = Path(title="The ID of the item to get")):
        self.id = id


class UpdateUserQueryParams:
    def __init__(self, id: str = Path(title="The ID of the item to get"), user: UpdateUser = Body(...)):
        self.id = id
        self.user = user
