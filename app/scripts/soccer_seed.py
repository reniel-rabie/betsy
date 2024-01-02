import os
import sys

# Add parent directory to path for imports
current_dir = os.path.dirname(os.path.realpath(__file__))
app_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(app_dir)

from database import Database
from clients import SoccerClient
from config import setup_logger

# Seed countries


if __name__ == "main":
    # Seed data into soccer databse
    logger = setup_logger(__file__.__name__)

    # use client to get data
    client = SoccerClient()
    countries_data = client.GET_country()

    # rework data

    # add data to database