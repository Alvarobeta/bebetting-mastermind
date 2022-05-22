import os

import uvicorn
from dotenv import load_dotenv
from fastapi_sqlalchemy import DBSessionMiddleware

from app.mastermind.infrastructure import config
from app.mastermind.infrastructure.FastAPI.fastapi_application import \
    FastAPIApplication
from app.mastermind.infrastructure.FastAPI.logger import setup_logging

setup_logging(config_file_path=config.LOGGING_CONFIG_FILE_PATH)

load_dotenv(".env")

# Expose app object to Http Server
app = FastAPIApplication()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8888)
