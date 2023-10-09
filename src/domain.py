from dataclasses import dataclass
from enums import Location, JobKeyword, LocationModifier


@dataclass(frozen=True)
class JobListing:
    title: str
    location: Location
    key_words: list[JobKeyword]


@dataclass(frozen=True)
class ProcessedMember:
    name: str
    locations: list[Location]
    location_modifiers: list[LocationModifier]
    job_keywords: list[JobKeyword]


@dataclass(frozen=True)
class JobRecommendation:
    title: str
    location: Location
    score: int


@dataclass(frozen=True)
class JobRecommendations:
    member_name: str
    job_recommendations: list[JobRecommendation]
