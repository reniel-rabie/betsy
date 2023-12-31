import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../app")))

from app.clients.football_client import FootballClient
from app.utils.my_types import *


class TestFootballClient(unittest.TestCase):
    def setUp(self):
        self.fc = FootballClient()

    def test_GET_country(self):
        country = self.fc.GET_country("US")
        self.assertIsInstance(country, Country)
        self.assertEqual(country.code, "US")
        self.assertEqual(country.name, "United States")
        self.assertEqual(country.id, 226)


if __name__ == "__main__":
    unittest.main()
