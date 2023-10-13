from domain import ProcessedMember
from enums import Location, LocationModifier
from shared import get_job_key_words_from_string
from utils import translator


def raw_members_to_processed_members(members_data: list) -> list[ProcessedMember]:
    members_data = [normalise_member_biography(member) for member in members_data]
    processed_members = process_raw_members(members_data=members_data)

    return processed_members


def normalise_member_biography(member: dict) -> dict:
    member["bio"] = member["bio"].translate(translator).upper().split()
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
    location_key_words = []
    valid_location_key_words = Location.list_values()
    for word in biography:
        if word in valid_location_key_words:
            location_key_words.append(Location[word])
    return location_key_words


def parse_location_modifiers(biography: str) -> list[LocationModifier]:
    location_modifiers = []
    valid_location_modifiers = LocationModifier.list_values()
    for word in biography:
        if word in valid_location_modifiers:
            location_modifiers.append(LocationModifier[word])
    return location_modifiers
