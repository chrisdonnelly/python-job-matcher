from dataclasses import dataclass
from enums import Location, JobTitleKeyword, LocationModifier


@dataclass(frozen=True)
class JobListing:
    title: str
    location: Location
    job_title_key_words: list[JobTitleKeyword]


@dataclass(frozen=True)
class Member:
    name: str
    locations: list[Location]
    location_modifiers: list[LocationModifier]
    job_keywords: list[JobTitleKeyword]


@dataclass(frozen=True)
class JobRecommendation:
    title: str
    location: Location
    score: int


@dataclass(frozen=True)
class JobRecommendations:
    member_name: str
    job_recommendations: list[JobRecommendation]
