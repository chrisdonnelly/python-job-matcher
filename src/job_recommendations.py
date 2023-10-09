from domain import ProcessedMember, JobListing, JobRecommendation, JobRecommendations
from enums import LocationModifier


def get_recommended_jobs(members: list[ProcessedMember], jobs: list[JobListing]):
    job_recommendations = []
    for member in members:
        recommended_jobs = [get_job_score(member=member, job=job) for job in jobs]
        highest_score = max(job.score for job in recommended_jobs)
        recommended_jobs_by_score = [
            job
            for job in recommended_jobs
            if job.score != 0 and job.score == highest_score
        ]
        job_recommendations.append(
            JobRecommendations(
                member_name=member.name, job_recommendations=recommended_jobs_by_score
            )
        )
    return job_recommendations


def get_job_score(member: ProcessedMember, job: JobListing) -> JobRecommendation | None:
    location_score = get_job_location_score(member=member, job=job)
    job_match_score = get_job_match_score(member=member, job=job)

    total_score = location_score + job_match_score

    return JobRecommendation(
        title=job.title, location=job.location.value, score=total_score
    )


def get_job_location_score(member: ProcessedMember, job: JobListing) -> int:
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


def get_job_match_score(member: ProcessedMember, job: JobListing) -> int:
    job_match_score = 0

    for key_word in member.job_keywords:
        match = [word for word in job.key_words if key_word.value in word.value]
        if len(match) > 0:
            job_match_score += len(match)
    return job_match_score
