from fastapi.encoders import jsonable_encoder
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.app_name.domain.domain_exception import DomainException


class CustomDomainExceptionHandler:
    def __call__(self, request: Request, exc: DomainException):
        return JSONResponse(
            status_code=exc.status,
            content=jsonable_encoder(
                {"error": {"type": exc.type, "message": exc.message}}
            ),
        )
