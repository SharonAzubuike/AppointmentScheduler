from datetime import datetime
from enum import Enum
from model.Client import Client
from model.Doctor import Doctor


class AppointmentRequest:
    def __init__(self, client: Client, doctor: Doctor, date_time_from: datetime, date_time_to: datetime):
        self.client = client
        self.doctor = doctor
        self.date_time_from = date_time_from
        self.date_time_to = date_time_to
        self.status = AppointmentRequestStatus.PENDING


class AppointmentRequestStatus(Enum):
    PENDING = 1
    ACCEPTED = 2
    DECLINED = 3
