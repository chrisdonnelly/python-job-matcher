from domain import JobListing
from enums import Location
from shared import get_job_key_words_from_string


def raw_jobs_to_processed_job_listings(jobs_data: list) -> list[JobListing]:
    return [
        JobListing(
            title=job["title"],
            location=get_job_location(job["location"]),
            job_title_key_words=get_job_key_words_from_string(job["title"]),
        )
        for job in jobs_data
    ]


def get_job_location(location: str) -> Location:
    for loc in Location:
        if loc.value.upper() == location.upper():
            return loc
    raise ValueError(f"Invalid location: {location}")
