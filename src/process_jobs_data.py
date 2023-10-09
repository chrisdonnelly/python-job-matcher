from domain import JobListing
from enums import Location
from shared import get_job_keywords


def raw_jobs_to_processed_job_listings(jobs_data: list) -> list[JobListing]:
    return [
        JobListing(
            title=job["title"],
            location=get_job_location(job["location"]),
            key_words=get_job_keywords(job["title"]),
        )
        for job in jobs_data
    ]


def get_job_location(location: str) -> Location:
    string_to_parse = location.upper()
    return getattr(Location, string_to_parse, None)
