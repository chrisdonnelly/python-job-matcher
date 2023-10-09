import enum


class ExtendedEnum(enum.Enum):
    @classmethod
    def list_values(cls):
        return [c.value for c in cls]


class JobKeyword(ExtendedEnum):
    SOFTWARE = "SOFTWARE"
    DEVELOPER = "DEVELOPER"
    MARKETING = "MARKETING"
    INTERNSHIP = "INTERNSHIP"
    DATA = "DATA"
    SCIENTIST = "SCIENTIST"
    LEGAL = "LEGAL"
    PROJECT = "PROJECT"
    MANAGER = "MANAGER"
    SALES = "SALES"
    UX = "UX"
    DESIGNER = "DESIGNER"
    DESIGN = "DESIGN"


class Location(ExtendedEnum):
    LONDON = "LONDON"
    YORK = "YORK"
    MANCHESTER = "MANCHESTER"
    EDINBURGH = "EDINBURGH"


class LocationModifier(ExtendedEnum):
    OUTSIDE = "OUTSIDE"
    RELOCATE = "RELOCATE"
