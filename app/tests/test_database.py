import os
import sys

# Add parent directory to path for imports
current_dir = os.path.dirname(os.path.realpath(__file__))
app_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(app_dir)

from database import Database
from unittest import TestCase

class TestDatabase(TestCase):
    def setUp(self) -> None:
        self.db = Database()

    def test_connect(self):
        pass