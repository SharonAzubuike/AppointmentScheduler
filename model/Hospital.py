from typing import List
from model.Department import Department


class Hospital:
    def __init__(self, name: str, departments: List[Department]):
        self.name = name
        self.departments = departments

    def __repr__(self):
        return f'Name: {self.name}\n' \
               f'Departments: {str(self.departments)}'
