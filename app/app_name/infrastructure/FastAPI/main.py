from app.app_name.infrastructure import config
from app.app_name.infrastructure.FastAPI.fastapi_application import \
    FastAPIApplication
from app.app_name.infrastructure.FastAPI.logger import setup_logging

setup_logging(config_file_path=config.LOGGING_CONFIG_FILE_PATH)

# Expose app object to Http Server
app = FastAPIApplication()
