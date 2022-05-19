from starlette.middleware.base import BaseHTTPMiddleware

from app.mastermind.infrastructure import config


class CustomServerHttpResponseHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["server"] = self._generate_slug(config.PROJECT_NAME)
        return response

    @staticmethod
    def _generate_slug(name: str) -> str:
        return name.replace(" ", "_").lower()
