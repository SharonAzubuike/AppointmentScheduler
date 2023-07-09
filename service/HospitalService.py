from datetime import datetime

from model.AppointmentRequest import AppointmentRequest
from model.Client import Client
from model.Doctor import AvailableTimeSlot
from model.Hospital import Hospital


class HospitalService:
    def __init__(self, hospital: Hospital):
        self.hospital = hospital
        self.clients = []
        self.appointment_requests = []

    def add_client(self, name: str, date_of_birth: datetime, existing_conditions: list, languages: list):
        client = Client(name, date_of_birth, existing_conditions, languages)
        self.clients.append(client)

    def get_hospital_information(self):
        return f'{self.hospital}'

    def book_appointment(self, client: Client, available_time_slot: AvailableTimeSlot):
        for department in self.hospital.departments:
            for doctor in department.doctors:
                if self.is_matching_doctor(client, doctor):
                    print("A doctor has been found for client")
                    if available_time_slot in doctor.available_time_slots:
                        appointment = AppointmentRequest(client, doctor, available_time_slot.date_time_from,
                                                         available_time_slot.date_time_to)
                        self.appointment_requests.append(appointment)
                        doctor.available_time_slots.remove(available_time_slot)
                        print("Appointment has been booked successfully.")
                        return
                    else:
                        print("Selected time slot is not available for this particular doctor.")
                        return
            print("Check again")

    @staticmethod
    def has_common_element(list1, list2):
        result = False
        for x in list1:
            for y in list2:
                if x == y:
                    result = True
                    return result
        return result

    def get_available_slots(self, client: Client, date_time_from: datetime, date_time_to: datetime):
        for department in self.hospital.departments:
            for doctor in department.doctors:
                for available_time_slot in doctor.available_time_slots:
                    for a in client.languages:
                        for b in doctor.languages:
                            if a == b:
                                return doctor.available_time_slots
                            else:
                                print("No matching language found")
                    for x in client.existing_conditions:
                        for y in doctor.qualifications:
                            for z in y.related_conditions:
                                if x == z:
                                    return doctor.available_time_slots
                                else:
                                    print("No Doctor available for the condition mentioned \n"
                                          "Please check again at a later time")
                                if available_time_slot == AvailableTimeSlot(date_time_from, date_time_to):
                                    return f'Available from {date_time_from} to {date_time_to}'
                            else:
                                print("false, start over")

    @staticmethod
    def is_within_range(available_time_slot, date_time_from, date_time_to):
        for time_slot in available_time_slot:
            if date_time_from <= time_slot <= date_time_to:
                return True
        return False

    @staticmethod
    def is_matching_doctor(client, doctor):
        language_match = False
        condition_match = False

        for x in client.existing_conditions:
            for y in doctor.qualifications:
                for z in y.related_conditions:
                    if x.name == z.name:
                        condition_match = True
        for a in client.languages:
            for b in doctor.languages:
                if a == b:
                    language_match = True
                break
        return language_match and condition_match
