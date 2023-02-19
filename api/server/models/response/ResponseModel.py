from fastapi import HTTPException


class ResponseModel:

    @staticmethod
    def success_response(data, message):
        return {
            "data": [data],
            "code": 200,
            "message": message
        }

    @staticmethod
    def error_response(error, http_type_error: HTTPException, message):
        return {
            "error": error,
            "http_type_error": http_type_error,
            "message": message
        }

    @staticmethod
    def updated_message(id: str):
        return {
            "message": "Student with ID: {} updated successfully".format(id),
        }

    @staticmethod
    def delete_message(id: str):
        return {
            "message": "Student with ID: {} delete successfully".format(id),
        }
