from fastapi.encoders import jsonable_encoder
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.mastermind.application.application_exception import ApplicationException


class CustomApplicationExceptionHandler:
    def __call__(self, request: Request, exc: ApplicationException):
        return JSONResponse(
            status_code=exc.status,
            content=jsonable_encoder(
                {"error": {"type": exc.type, "message": exc.message}}
            ),
        )
