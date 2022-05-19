import os

import uvicorn
from dotenv import load_dotenv
from fastapi_sqlalchemy import DBSessionMiddleware, db

from app.mastermind.infrastructure import config
from app.mastermind.infrastructure.FastAPI.fastapi_application import \
    FastAPIApplication
from app.mastermind.infrastructure.FastAPI.logger import setup_logging
from models import User as ModelUser
from schema import User as SchemaUser

setup_logging(config_file_path=config.LOGGING_CONFIG_FILE_PATH)

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# load_dotenv(os.path.join(BASE_DIR, ".env"))

load_dotenv(".env")

# Expose app object to Http Server
app = FastAPIApplication()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


# @app.post("/user/", response_model=SchemaUser)
# def create_user(user: SchemaUser):
#     db_user = ModelUser(
#         first_name=user.first_name, last_name=user.last_name, age=user.age
#     )
#     db.session.add(db_user)
#     db.session.commit()
#     return db_user


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8888)
