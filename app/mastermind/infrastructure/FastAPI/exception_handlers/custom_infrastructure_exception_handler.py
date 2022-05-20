from fastapi.encoders import jsonable_encoder
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.mastermind.infrastructure.infrastructure_exception import \
    InfrastructureException


class CustomInfrastructureExceptionHandler:
    def __call__(self, request: Request, exc: InfrastructureException):
        return JSONResponse(
            status_code=exc.status,
            content=jsonable_encoder(
                {"error": {"type": exc.type, "message": exc.message}}
            ),
        )
