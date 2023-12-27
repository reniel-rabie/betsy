from typing import TypedDict
from enum import Enum
from datetime import datetime


class Sport(Enum):
    FOOTBALL = "football"
    BASKETBALL = "basketball"
    BASEBALL = "baseball"


class LeagueType(Enum):
    LEAGUE = "League"
    CUP = "Cup"
    SUPER_CUP = "Super Cup"
    PLAYOFF = "Playoff"


class FixtureStatus(Enum):
    NOT_STARTED = "NS"
    IN_PLAY = "IN_PLAY"
    PAUSED = "PAUSED"
    FINISHED = "FT"
    POSTPONED = "PST"
    SUSPENDED = "SUSP"
    CANCELED = "CANC"


class Country(TypedDict):
    code: str
    name: str


class Team(TypedDict):
    id: int
    name: str
    code: str
    sport: Sport
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
    home_team_id: int
    away_team_id: int
    timestamp: int
    status: FixtureStatus
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
    sport: Sport
    home_win: float
    draw: float
    away_win: float
    bookmaker_id: int
