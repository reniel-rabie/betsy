import os
import sys
import pandas as pd
import numpy as np

# Add parent directory to path for imports
current_dir = os.path.dirname(os.path.realpath(__file__))
app_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(app_dir)

from clients import FootballClient
from database import Database

# from database import Database

db = Database()
fc = FootballClient()

# Countries to be seeded into the database
countries_entries = [
    {
        "name": "England",
        "code": "GB",
    },
    {
        "name": "Spain",
        "code": "ES",
    },
    {
        "name": "Germany",
        "code": "DE",
    },
    {
        "name": "Italy",
        "code": "IT",
    },
    {
        "name": "France",
        "code": "FR",
    },
    {
        "name": "Portugal",
        "code": "PT",
    },
    {
        "name": "Netherlands",
        "code": "NL",
    },
    {
        "name": "Argentina",
        "code": "AR",
    },
    {
        "name": "Brazil",
        "code": "BR",
    },
    {
        "name": "United States",
        "code": "US",
    },
]

# Leagues to be seeded into the database
leagues_entries = [
    {
        "name": "Premier League",
        "country_code": "GB",
    },
    {
        "name": "La Liga",
        "country_code": "ES",
    },
    {
        "name": "Bundesliga",
        "country_code": "DE",
    },
    {
        "name": "Serie A",
        "country_code": "IT",
    },
    {
        "name": "Ligue 1",
        "country_code": "FR",
    },
    {
        "name": "Primeira Liga",
        "country_code": "PT",
    },
    {
        "name": "Eredivisie",
        "country_code": "NL",
    },
    {
        "name": "Major League Soccer",
        "country_code": "US",
    },
]

# Dataframe columns
# historical data
tables = db.table_names()
columns = {}
for table in tables:
    columns[table] = db.columns(table)

print(columns["countries"])

countries = pd.DataFrame(columns=columns["countries"])
venues = pd.DataFrame(columns=columns["venues"])
leagues = pd.DataFrame(columns=columns["leagues"])
seasons = pd.DataFrame(columns=columns["seasons"])
teams = pd.DataFrame(columns=columns["teams"])
football_fixtures = pd.DataFrame(columns=columns["football_fixtures"])

# get country data
for country in countries_entries:
    data = fc.GET_country(country["code"])
    countries = countries.append(data, ignore_index=True)

print("Countries:", countries.head(5))

# Work football fixture data for training model
