from datetime import datetime
from typing import List

from model.Condition import Condition
from model.Language import Language


class Client:
    def __init__(self, name: str, date_of_birth: datetime, existing_conditions: List[Condition],
                 languages: List[Language]):
        self.name = name
        self.date_of_birth = date_of_birth
        self.existing_conditions = existing_conditions
        self.languages = languages

    def __repr__(self):
        return f'Client Name: {self.name}\n' \
               f'Date of Birth: {self.date_of_birth}\n' \
               f'Existing Conditions: {str(self.existing_conditions)}\n' \
               f'Spoken Languages: {str(self.languages)}'
