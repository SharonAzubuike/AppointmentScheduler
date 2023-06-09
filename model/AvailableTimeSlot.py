from datetime import datetime


class AvailableTimeSlot:
    def __init__(self, date_time_from: datetime, date_time_to: datetime):
        self.date_time_from = date_time_from
        self.date_time_to = date_time_to

    def __repr__(self):
        return f'Available from {self.date_time_from} to {self.date_time_to}'
