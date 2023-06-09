from enum import Enum


class AppointmentSchedulerAction(Enum):
    EXIT = 0
    LIST_ACTIONS = 1
    ADD_CLIENT = 2
    LIST_CLIENTS = 3
    BOOK_APPOINTMENT = 4
    PRINT_HOSPITAL_INFORMATION = 5
    LIST_APPOINTMENTS = 6

    def __repr__(self):
        return f'{self.value} - {self.name}'
