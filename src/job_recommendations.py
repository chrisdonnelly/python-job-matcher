from domain import Member, JobListing, JobRecommendation, JobRecommendations
from enums import LocationModifier
from typing import Literal


def get_recommended_jobs_for_members(members: list[Member], jobs: list[JobListing]):
    recommendations = []
    for member in members:
        member_recommendations = []

        for job in jobs:
            # Calculate score for shared job title key words
            keyword_score = get_job_title_key_words_score(member=member, job=job)

            # Calculate location score
            location_score = get_location_score(member=member, job=job)

            # Combine keyword score and location score
            total_score = keyword_score + location_score

            # Create a job recommendation
            if total_score > 0:
                recommendation = JobRecommendation(
                    title=job.title, location=job.location, score=total_score
                )
                member_recommendations.append(recommendation)

        # Sort recommendations by total score in descending order
        member_recommendations.sort(key=lambda x: x.score, reverse=True)

        # Find the highest-scoring jobs
        highest_score = member_recommendations[0].score if member_recommendations else 0
        highest_scorers = [
            rec for rec in member_recommendations if rec.score == highest_score
        ]

        # Limit the number of recommendations, e.g., top 3 highest-scoring jobs
        highest_scorers = highest_scorers[:3]

        recommendations.append(
            JobRecommendations(
                member_name=member.name, job_recommendations=highest_scorers
            )
        )

    return recommendations


def get_job_title_key_words_score(member: Member, job: JobListing) -> int:
    keyword_scores = [
        1 if member_kw.value in job_kw.value else 0
        for member_kw in member.job_keywords
        for job_kw in job.job_title_key_words
    ]
    keyword_score = sum(keyword_scores)

    return keyword_score


def get_location_score(member: Member, job: JobListing) -> Literal[0, -1, 1]:
    if not member.locations:
        return 0  # No location preference, no location score

    if LocationModifier.OUTSIDE in member.location_modifiers:
        return (
            -1 if job.location in member.locations else 0
        )  # Penalty for locations inside named location
    else:
        return (
            1 if job.location in member.locations else 0
        )  # Reward for locations inside preferred location
