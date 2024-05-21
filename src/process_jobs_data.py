from domain import JobListing
from enums import Location
from shared import get_job_title_key_words_from_string


def get_normalised_jobs_from_raw_data(raw_jobs_data: list) -> list[JobListing]:
    return [
        JobListing(
            title=job["title"],
            location=get_job_location(job["location"]),
            job_title_key_words=get_job_title_key_words_from_string(job["title"]),
        )
        for job in raw_jobs_data
    ]


def get_job_location(location: str) -> Location:
    for loc in Location:
        if loc.value.upper() == location.upper():
            return loc
    raise ValueError(f"Invalid location: {location}")
