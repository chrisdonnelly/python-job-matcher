from http_client import fetch_json_data
import os
import pprint
from process_jobs_data import get_normalised_jobs_from_raw_data
from process_members_data import get_normalised_members_from_raw_data
from job_recommendations import get_recommended_jobs_for_members
import time


def main():
    start_time = time.monotonic()
    jobs_url = os.environ.get("JOBS_URL")
    members_url = os.environ.get("MEMBERS_URL")

    raw_jobs_data = fetch_json_data(url=jobs_url)
    raw_members_data = fetch_json_data(url=members_url)

    normalised_jobs = get_normalised_jobs_from_raw_data(jobs_data=raw_jobs_data)
    normalised_members = get_normalised_members_from_raw_data(
        members_data=raw_members_data
    )

    job_recommendations = get_recommended_jobs_for_members(
        members=normalised_members, jobs=normalised_jobs
    )

    pp = pprint.PrettyPrinter(indent=6)
    for job in job_recommendations:
        pp.pprint(job)
    print(
        f"{len(job_recommendations)} job recommendations created in {int(time.monotonic() - start_time)}s."
    )


main()
