import os
import sys
import pandas as pd
from itertools import chain

# Add parent directory to path for imports
current_dir = os.path.dirname(os.path.realpath(__file__))
app_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(app_dir)

from database import Database
from clients import SoccerClient
from config import setup_logger


COUNTRY_CODES = [
    "US",
    "AR",
    "BR",
    "NL",
    "FR",
    "PT",
    "DE",
    "IT",
    "ES",
    "GB",
    "AT",
]

# initialize client and database
client = SoccerClient()
db = Database()
db.connect()

# Countries
# countries_columns = db.columns("countries")
# countries = [pd.Series(client.get_country(code)) for code in COUNTRY_CODES]
# countries_df = pd.DataFrame(countries, columns=countries_columns)
# db.insert("countries", countries_df)

# Leagues
leagues_columns = db.columns("leagues")
leagues = [pd.Series(client.get_league(code, 2)) for code in COUNTRY_CODES]
leagues = [element for sublist in leagues for element in sublist]
leagues_df = pd.DataFrame(leagues, columns=leagues_columns)
print(leagues_df.loc[0])
db.insert("leagues", leagues_df)

# finally close database connection
db.close()
