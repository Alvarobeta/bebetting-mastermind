import json
import logging
import logging.config
import os

from app.mastermind.infrastructure import config


def setup_logging(config_file_path: str):
    absolute_config_file_path = config.PROJECT_PATH + "/" + config_file_path

    if not os.path.exists(absolute_config_file_path):
        raise RuntimeError(f"There is not file at: {absolute_config_file_path}")

    with open(absolute_config_file_path, "rt") as f:
        config_file = json.load(f)
        logging.config.dictConfig(config_file)
