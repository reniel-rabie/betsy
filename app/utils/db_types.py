from typing import TypedDict
from enum import Enum
from datetime import datetime


class SportType(Enum):
    FOOTBALL = "football"
    BASKETBALL = "basketball"
    BASEBALL = "baseball"


class LeagueType(Enum):
    LEAGUE = "League"
    CUP = "Cup"
    SUPER_CUP = "Super Cup"
    PLAYOFF = "Playoff"


class Country(TypedDict):
    code: str
    name: str


class Team(TypedDict):
    id: int
    name: str
    code: str
    sport: SportType
    venue_id: int


class League(TypedDict):
    id: int
    name: str
    type: LeagueType
    country_code: str


class Season(TypedDict):
    league_id: int
    year: int
    start: datetime
    end: datetime


class Venue(TypedDict):
    id: int
    name: str
    city_name: str


class Fixture(TypedDict):
    id: int
    sport: SportType
    home_team_id: int
    away_team_id: int
    timestamp: int
    status: str
    venue_id: int
    home_team_score: int
    away_team_score: int
    home_team_half_score: int
    away_team_half_score: int


class Bookmaker(TypedDict):
    id: int
    name: str


class Odds(TypedDict):
    fixture_id: int
    sport: SportType
    home_win: float
    draw: float
    away_win: float
    bookmaker_id: int
