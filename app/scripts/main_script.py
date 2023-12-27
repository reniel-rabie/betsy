import os
import sys

# Add parent directory to path for imports
current_dir = os.path.dirname(os.path.realpath(__file__))
app_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(app_dir)

from config import setup_logger
from clients import FootballClient

logger = setup_logger(__name__)
logger.info("Starting main script")
fc = FootballClient()
