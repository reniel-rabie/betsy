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
from utils.my_types import *

load_dotenv()


class FootballClient:
    def __init__(self) -> None:
        self.base_url = "api-football-v1.p.rapidapi.com"
        self.api_key = os.getenv("X-RapidAPI-Key")
        self.headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": self.base_url,
        }
        self.conn = http.client.HTTPSConnection(self.base_url)
        self.logger = setup_logger(self.__class__.__name__)

    def GET(self, endpoint):
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

    def GET_league(self, league_name: str, country_code: str):
        """Get all leagues"""
        league_name = league_name.replace(" ", "%20")
        endpoint = f"/v3/leagues?name={league_name}&code={country_code}"
        league = self.GET(endpoint)[0]["league"]
        league = League(
            id=league["id"],
            name=league["name"],
            type=LeagueType(league["type"]),
        )
        self.logger.info(f"GET_league returned {league}")
        return league

    def GET_seasons(self, league_id: int):
        """Get all seasons with statistical analysis for a league"""
        endpoint = f"/v3/leagues?id={league_id}"
        data = self.GET(endpoint)
        seasons = []
        for season in data[0]["seasons"]:
            if season["coverage"]["fixtures"]["statistics_fixtures"] == True:
                seasons.append(season["year"])

        self.logger.info(f"GET_seasons returned {seasons}")
        return seasons

    def GET_teams(self, league_id: int, season: int):
        """Get all teams for a league and season"""
        endpoint = f"/v3/teams?league={league_id}&season={season}"
        data = self.GET(endpoint)
        teams = []
        for team in data:
            teams.append(
                Team(
                    id=team["team"]["id"],
                    name=team["team"]["name"],
                    venue_name=team["venue"]["name"],
                )
            )
        self.logger.info(f"GET_teams returned {teams}")
        return teams

    def GET_fixtures(self, league_id: int, season: int):
        """Get all fixtures for a league and season"""
        # Check for valid season
        if len(str(season)) != 4 or season < 2000 or season > datetime.now().year:
            self.logger.error(f"Invalid season: {season}")
            return

        endpoint = f"/v3/fixtures?league={league_id}&season={season}"
        data = self.GET(endpoint)
        fixtures = []
        n = 0
        for fixture in data:
            n += 1
            print(n)
            fixtures.append(
                Match(
                    id=fixture["fixture"]["id"],
                    home_team_id=fixture["teams"]["home"]["id"],
                    away_team_id=fixture["teams"]["away"]["id"],
                    time=datetime.strptime(
                        fixture["fixture"]["date"], "%Y-%m-%dT%H:%M:%S%z"
                    ),
                    status=MatchStatus(fixture["fixture"]["status"]["short"]),
                    venue_id=fixture["fixture"]["venue"]["id"],
                    home_team_score=fixture["goals"]["home"],
                    away_team_score=fixture["goals"]["away"],
                )
            )

        # self.logger.info(f"GET_fixtures returned {fixtures}")
        # self.logger.info(f"GET_fixtures returned {len(fixtures)} fixtures")

        return fixtures


if __name__ == "__main__":
    fc = FootballClient()
    fc.GET_fixtures(39, 2021)
