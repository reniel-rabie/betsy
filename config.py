import os
import logging
from logging.handlers import RotatingFileHandler

# create necessary directories
dirs = [
    'logs'
]
for dir in dirs:
    dir_name = os.path.join(os.getcwd(), dir)
    os.makedirs(dir_name, exist_ok=True)

# configure basic logger
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def setup_logger(name: str) -> logging.Logger:
    # format name
    name = name.replace('_', '')

    # create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # formatter
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

    # console handler
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)

    # file handler
    log_file = os.path.join(os.getcwd(), 'logs', f"{name}.log")
    file_handler = RotatingFileHandler(
        filename=log_file,
        maxBytes=1024 * 1024,
        backupCount=10
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger