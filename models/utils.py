def response(data: dict, message: str) -> dict:
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def error_response(error: str, code: str, message: str) -> dict:
    return {"error": error, "code": code, "message": message}
