from http_client import fetch_json_data
import os
import pprint
from process_jobs_data import raw_jobs_to_processed_job_listings
from process_members_data import raw_members_to_processed_members
from job_recommendations import get_recommended_jobs


def main():
    jobs_url = os.environ.get("JOBS_URL")
    members_url = os.environ.get("MEMBERS_URL")

    jobs_data = fetch_json_data(url=jobs_url)
    members_data = fetch_json_data(url=members_url)

    processed_jobs = raw_jobs_to_processed_job_listings(jobs_data=jobs_data)
    processed_members = raw_members_to_processed_members(members_data=members_data)

    job_recommendations = get_recommended_jobs(
        members=processed_members, jobs=processed_jobs
    )

    pp = pprint.PrettyPrinter(indent=12)
    pp.pprint(job_recommendations)


main()
