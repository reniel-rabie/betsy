import os
import sys
import http.client
import json
from dotenv import load_dotenv
from datetime import datetime

# Add parent directory to path for imports
current_dir = os.path.dirname(os.path.realpath(__file__))
app_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(app_dir)

from config import setup_logger
from lib.db_types import *
from database import Database

load_dotenv()


class SoccerClient:
    def __init__(self) -> None:
        self.base_url = "api-football-v1.p.rapidapi.com"
        self.api_key = os.getenv("X-RapidAPI-Key")
        self.headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": self.base_url,
        }
        self.conn = http.client.HTTPSConnection(self.base_url)
        self.db = Database()
        self.logger = setup_logger(self.__class__.__name__)

    def __GET(self, endpoint):
        """GET Requests to football API"""
        self.conn.request("GET", endpoint, headers=self.headers)
        # Convert resp to JSON
        resp = self.conn.getresponse().read()
        data = json.loads(resp)
        if data["results"] == 0:
            self.logger.warning(f"GET {endpoint} returned no results")
        if data["errors"]:
            self.logger.error(f"GET {endpoint} returned errors: {data['errors']}")
        if data["response"]:
            self.logger.info(f"GET {endpoint} returned {data['results']} results")
        return data["response"]

    def get_country(self, country_code: str):
        """Get country by code"""
        if len(country_code) != 2:
            self.logger.error(f"Invalid country code: {country_code}")
            return

        endpoint = f"/v3/countries?code={country_code}"
        response = self.__GET(endpoint)
        country = Country(
            name=response[0]["name"],
            code=response[0]["code"],
        )
        self.logger.info(f"get_country returned {country}")
        return country

    def get_countries(self):
        """Get all countries"""
        endpoint = f"/v3/countries"
        data = self.__GET(endpoint)
        countries = [
            Country(name=country["name"], code=country["code"]) for country in data
        ]
        self.logger.info(f"get_countries returned {len(countries)} results")
        return countries

    def get_venues(self, country_name: str):
        """Get venue by country name"""
        endpoint = f"/v3/venues?country={country_name}"
        response = self.__GET(endpoint)
        venues = [
            Venue(
                id=venue["id"],
                name=venue["name"],
                city_name=venue["city"],
            )
            for venue in response
        ]
        return venues

    def get_league(self, country_code: str, amount: int = 1) -> list[League]:
        """Get all leagues"""
        self.db.connect()
        endpoint = f"/v3/leagues?code={country_code}"
        response = self.__GET(endpoint)
        if amount > len(response):
            amount = len(response)

        leagues = [
            League(
                id=int(league["league"]["id"]),
                sport=SportType.SOCCER.value,
                name=league["league"]["name"],
                country_id=self.db.get(
                    "countries", where={"code": league["country"]["code"]}
                ).loc[0, "uuid"],
                type=LeagueType(league["league"]["type"]).value,
            )
            for league in response[:amount]
        ]
        # self.logger.info(f"get_league returned {leagues}")
        print("first league", leagues[0])
        self.db.close()
        return leagues

    def get_seasons(self, league_id: int):
        """Get all seasons with statistical analysis for a league"""
        endpoint = f"/v3/leagues?id={league_id}"
        data = self.__GET(endpoint)
        seasons = []
        for season in data[0]["seasons"]:
            if season["coverage"]["fixtures"]["statistics_fixtures"] == True:
                seasons.append(season["year"])

        self.logger.info(f"get_seasons returned {seasons}")
        return seasons

    def get_teams(self, league_id: int, season: int):
        """Get all teams for a league and season"""
        endpoint = f"/v3/teams?league={league_id}&season={season}"
        data = self.__GET(endpoint)
        teams = []
        for team in data:
            teams.append(
                Team(
                    id=team["team"]["id"],
                    name=team["team"]["name"],
                    venue_name=team["venue"]["name"],
                )
            )
        self.logger.info(f"get_teams returned {teams}")
        return teams

    def get_fixtures(self, league_id: int, season: int):
        """Get all fixtures for a league and season"""
        # Check for valid season
        if len(str(season)) != 4 or season < 2000 or season > datetime.now().year:
            self.logger.error(f"Invalid season: {season}")
            return

        endpoint = f"/v3/fixtures?league={league_id}&season={season}"
        data = self.__GET(endpoint)
        fixtures: list[Fixture] = [
            Fixture(
                id=fixture["fixture"]["id"],
                home_team_id=fixture["teams"]["home"]["id"],
                away_team_id=fixture["teams"]["away"]["id"],
                timestamp=fixture["fixture"]["timestamp"],
                status=fixture["fixture"]["status"]["short"],
                venue_id=fixture["fixture"]["venue"]["id"],
                home_team_score=fixture["goals"]["home"],
                away_team_score=fixture["goals"]["away"],
                home_team_half_score=fixture["score"]["halftime"]["home"],
                away_team_half_score=fixture["score"]["halftime"]["away"],
            )
            for fixture in data
            if fixture["fixture"]["timestamp"]
        ]

        self.logger.info(
            f"get_fixtures returned {fixtures} for league {league_id}, season {season}"
        )
        self.logger.info(f"get_fixtures returned {len(fixtures)} fixtures")

        return fixtures


if __name__ == "__main__":
    client = SoccerClient()
