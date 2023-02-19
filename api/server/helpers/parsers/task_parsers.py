def task_parser(task) -> dict:
    return {
        "id": str(task["_id"]),
        "name": task["name"],
        "status": task["status"],
        "description": task["description"],
    }