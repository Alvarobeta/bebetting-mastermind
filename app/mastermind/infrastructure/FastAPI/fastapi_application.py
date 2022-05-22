from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.gzip import GZipMiddleware

from app.mastermind.domain.domain_exception import DomainException
from app.mastermind.infrastructure import config
from app.mastermind.infrastructure.FastAPI.api_v1.api import api_router
from app.mastermind.infrastructure.FastAPI.exception_handlers.custom_domain_exception_handler import \
    CustomDomainExceptionHandler
from app.mastermind.infrastructure.FastAPI.exception_handlers.request_validation_error_handler import \
    RequestValidationErrorHandler
from app.mastermind.infrastructure.FastAPI.middlewares.custom_server_http_response_header_middleware import \
    CustomServerHttpResponseHeaderMiddleware


class FastAPIApplication(FastAPI):
    def __init__(self):
        super().__init__(
            version=config.PROJECT_VERSION,
            title=config.PROJECT_NAME,
            description=config.PROJECT_DESCRIPTION,
            contact={
                "name": config.PROJECT_CONTACT_NAME,
                "email": config.PROJECT_CONTACT_EMAIL,
            },
            openapi_url="/api/v1/openapi.json",
        )

        self._add_exception_handlers()
        self._add_middlewares()
        self._add_routers()

    def _add_exception_handlers(self):
        self.add_exception_handler(DomainException, CustomDomainExceptionHandler())
        self.add_exception_handler(
            RequestValidationError, RequestValidationErrorHandler()
        )

    def _add_middlewares(self):
        self.add_middleware(GZipMiddleware)
        self.add_middleware(CustomServerHttpResponseHeaderMiddleware)

    def _add_routers(self):
        self.include_router(api_router, prefix=config.API_V1_STR)
