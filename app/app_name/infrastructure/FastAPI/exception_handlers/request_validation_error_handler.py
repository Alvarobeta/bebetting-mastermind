from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse


class RequestValidationErrorHandler:
    def __call__(self, request: Request, exc: RequestValidationError):
        error: dict = exc.errors()[0]

        error_location: str = ".".join(str(s) for s in error["loc"])
        error_message: str = error["msg"]

        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=jsonable_encoder(
                {
                    "error": {
                        "type": "invalid_request",
                        "message": f"On {error_location}, {error_message}",
                    }
                }
            ),
        )
