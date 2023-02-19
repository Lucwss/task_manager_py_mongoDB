def user_parser(user) -> dict:
    return {
        "id": str(user["_id"]),
        "user_name": user["user_name"],
        "email": user["email"],
        "tasks": user["tasks"],
        "birthdate": user["birthdate"],
        "hashed_password": user["hashed_password"],
        "disabled": user["disabled"]
    }

