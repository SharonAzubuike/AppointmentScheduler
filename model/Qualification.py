from typing import List

from model.Condition import Condition


class Qualification:
    def __init__(self, name: str, related_conditions: List[Condition]):
        self.name = name
        self.related_conditions = related_conditions

    def __repr__(self):
        return f'Qualification: {self.name}\n' \
               f'Related Conditions: {self.related_conditions}'
