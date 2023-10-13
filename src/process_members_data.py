from domain import ProcessedMember
from enums import Location, LocationModifier
from shared import get_job_key_words_from_string
from utils import translator


def raw_members_to_processed_members(members_data: list) -> list[ProcessedMember]:
    members_data = [normalise_member_biography(member) for member in members_data]
    processed_members = process_raw_members(members_data=members_data)

    return processed_members


def normalise_member_biography(member: dict) -> dict:
    member["bio"] = member["bio"].translate(translator).upper()
    return member


def process_raw_members(members_data: list) -> list[ProcessedMember]:
    processed_members = [
        ProcessedMember(
            name=member["name"],
            locations=member_locations_to_domain_locations(member["bio"]),
            location_modifiers=parse_location_modifiers(member["bio"]),
            job_keywords=get_job_key_words_from_string(member["bio"]),
        )
        for member in members_data
    ]

    return processed_members


def member_locations_to_domain_locations(biography: str) -> list[Location]:
    parsed_bio_content = biography.upper().split()
    location_keywords = [loc for loc in Location if loc.value in parsed_bio_content]
    return location_keywords


def parse_location_modifiers(biography: str) -> list[LocationModifier]:
    bio_content = biography.split()
    location_modifier_keywords = [
        loc for loc in LocationModifier if loc.value in bio_content
    ]
    return location_modifier_keywords
