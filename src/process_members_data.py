from domain import ProcessedMember
from enums import Location, LocationModifier
from shared import get_job_keywords
from utils import translator


def raw_members_to_processed_members(members_data: list) -> list[ProcessedMember]:
    members_data = biographies_to_uppercase(members_data=members_data)
    processed_members = process_raw_members(members_data=members_data)

    return processed_members


def biographies_to_uppercase(members_data: list) -> list[dict[str, any]]:
    members_data = [
        {"name": member["name"], "bio": member["bio"].upper()}
        for member in members_data
    ]
    return members_data


def process_raw_members(members_data: list) -> list[ProcessedMember]:
    processed_members = [
        ProcessedMember(
            name=member["name"],
            locations=parse_locations(member["bio"]),
            location_modifiers=parse_location_modifiers(member["bio"]),
            job_keywords=get_job_keywords(member["bio"]),
        )
        for member in members_data
    ]
    return processed_members


def parse_locations(bio: str) -> list[Location]:
    parsed_bio_content = bio.translate(translator).split()
    location_key_words = [
        getattr(Location, word, None)
        for word in parsed_bio_content
        if word in Location.list_values()
    ]
    return location_key_words


def parse_location_modifiers(bio: str) -> list[LocationModifier]:
    bio_content = bio.split()
    location_modifier_key_words = [
        getattr(LocationModifier, word, None)
        for word in bio_content
        if word in LocationModifier.list_values()
    ]
    return location_modifier_key_words
