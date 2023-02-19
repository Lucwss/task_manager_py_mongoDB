from ..User import User


class UserInDb(User):
    hashed_password: str
