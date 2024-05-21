from domain import Member
from enums import Location, LocationModifier
from shared import get_job_title_key_words_from_string
from utils import translator


def get_normalised_members_from_raw_data(members_data: list) -> list[Member]:
    members_data = [
        _strip_punctuation_from_member_bio(member=member) for member in members_data
    ]
    members = normalise_raw_members(members_data=members_data)

    return members


def normalise_raw_members(members_data: list) -> list[Member]:
    processed_members = [
        Member(
            name=member["name"],
            locations=_member_bio_locations_to_domain_locations(member["bio"]),
            location_modifiers=_parse_location_modifiers(member["bio"]),
            job_keywords=get_job_title_key_words_from_string(member["bio"]),
        )
        for member in members_data
    ]

    return processed_members


def _member_bio_locations_to_domain_locations(biography: str) -> list[Location]:
    parsed_bio_content = biography.upper().split()
    location_keywords = [loc for loc in Location if loc.value in parsed_bio_content]
    return location_keywords


def _parse_location_modifiers(biography: str) -> list[LocationModifier]:
    bio_content = biography.split()
    location_modifier_keywords = [
        loc for loc in LocationModifier if loc.value in bio_content
    ]
    return location_modifier_keywords


def _strip_punctuation_from_member_bio(member: dict) -> dict:
    member["bio"] = member["bio"].translate(translator).upper()
    return member
