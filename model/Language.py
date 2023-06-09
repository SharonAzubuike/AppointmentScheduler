from enum import Enum


class Language(Enum):
    ENGLISH = 1
    GERMAN = 2
    FRENCH = 3
    TURKISH = 4
    ARABIC = 5
    ITALIAN = 6

    def __repr__(self):
        return self.name
