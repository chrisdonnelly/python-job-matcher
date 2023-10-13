from domain import ProcessedMember, JobListing, JobRecommendation, JobRecommendations
from enums import LocationModifier


def get_recommended_jobs_for_members(
    members: list[ProcessedMember], jobs: list[JobListing]
):
    job_recommendations = []
    for member in members:
        recommended_jobs = [get_total_job_score(member=member, job=job) for job in jobs]
        recommended_jobs_filtered = filter_job_recommendations_by_score(
            recommended_jobs
        )
        job_recommendations.append(
            JobRecommendations(
                member_name=member.name, job_recommendations=recommended_jobs_filtered
            )
        )
    return job_recommendations


def filter_job_recommendations_by_score(
    recommended_jobs: list[JobRecommendation | None],
) -> list[JobRecommendation]:
    recommended_jobs = [job for job in recommended_jobs if job]

    if not recommended_jobs:
        return []

    highest_score = max(job.score for job in recommended_jobs if job)
    recommended_jobs_by_score = [
        job
        for job in recommended_jobs
        if job and job.score != 0 and job.score == highest_score
    ]

    return recommended_jobs_by_score


def get_total_job_score(
    member: ProcessedMember, job: JobListing
) -> JobRecommendation | None:
    location_score = get_job_location_score_for_member(member=member, job=job)
    job_match_score = get_job_keyword_match_score_for_member(member=member, job=job)

    total_score = location_score + job_match_score

    return JobRecommendation(title=job.title, location=job.location, score=total_score)


def get_job_location_score_for_member(member: ProcessedMember, job: JobListing) -> int:
    location_score = 0

    if (
        LocationModifier.OUTSIDE in member.location_modifiers
        and job.location not in member.locations
    ):
        location_score += 1
        return location_score

    if job.location in member.locations:
        location_score += 1

    return location_score


def get_job_keyword_match_score_for_member(
    member: ProcessedMember, job: JobListing
) -> int:
    job_match_score = 0
    for key_word in member.job_keywords:
        match = [word for word in job.key_words if key_word.value in word.value]
        if len(match) > 0:
            job_match_score += len(match)
    return job_match_score
