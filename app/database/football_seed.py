from football_client import FootballClient

# from database import Database

# dbs = Database()
fc = FootballClient()

# Countries to be seeded into the database
countries = [
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
leagues = [
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

# for league in leagues:
#     fc.GET_league(league["name"], league["country_code"])

# fc.GET_seasons(39)

# fc.GET_teams(39, 2021)

fix = fc.GET_fixtures(39, 2021)
print(len(fix))
