from datetime import datetime

from model.Condition import Condition
from model.Department import Department
from model.Doctor import Doctor
from model.Hospital import Hospital
from model.Language import Language
from model.Qualification import Qualification


def create_test_hospital():
    department1 = Department("Geriatrics", create_doctors())
    # department2 = Department("Psychiatry", create_doctors())
    return Hospital("Isarkrankenhaus", [department1])


def create_doctors():
    headache = Condition("headache")
    back_pain = Condition("back pain")
    copd = Condition("copd")
    cough = Condition("cough")
    cold = Condition("cold")
    hypertension = Condition("hypertension")
    conditions = [headache, back_pain, copd, cough, hypertension, cold]
    conditions1 = [headache, back_pain]
    languages = [Language.ENGLISH, Language.GERMAN]

    doctors = []

    qualification1 = Qualification("someCertificate", conditions1)
    doctor1 = Doctor("John Doe", "male", [qualification1], languages)
    doctor1.add_available_time_slot(datetime(2023, 6, 4, 8, 30), datetime(2023, 6, 4, 9, 0))
    doctor1.add_available_time_slot(datetime(2023, 6, 4, 10, 30), datetime(2023, 6, 4, 11, 0))
    doctor1.add_available_time_slot(datetime(2023, 6, 4, 14, 30), datetime(2023, 6, 4, 15, 0))
    doctor1.add_available_time_slot(datetime(2023, 6, 5, 8, 30), datetime(2023, 6, 5, 9, 0))
    doctor1.add_available_time_slot(datetime(2023, 6, 5, 10, 30), datetime(2023, 6, 5, 11, 0))
    doctor1.add_available_time_slot(datetime(2023, 6, 5, 14, 30), datetime(2023, 6, 5, 15, 0))
    doctors.append(doctor1)

    qualification2 = Qualification("someOtherCertificate", [Condition("Depression")])
    doctor2 = Doctor("Jane Doe", "female", [qualification2], languages)
    doctor2.add_available_time_slot(datetime(2023, 6, 4, 9, 30), datetime(2023, 6, 4, 10, 0))
    doctor2.add_available_time_slot(datetime(2023, 6, 4, 11, 30), datetime(2023, 6, 4, 12, 0))
    doctor2.add_available_time_slot(datetime(2023, 6, 4, 15, 30), datetime(2023, 6, 4, 16, 0))
    doctor2.add_available_time_slot(datetime(2023, 6, 5, 9, 30), datetime(2023, 6, 5, 10, 0))
    doctor2.add_available_time_slot(datetime(2023, 6, 5, 11, 30), datetime(2023, 6, 5, 12, 0))
    doctor2.add_available_time_slot(datetime(2023, 6, 5, 15, 30), datetime(2023, 6, 5, 16, 0))
    doctors.append(doctor2)

    qualification3 = Qualification("someCertificate", conditions)
    doctor3 = Doctor("Jannie Doyle", "female", [qualification3], languages)
    doctor3.add_available_time_slot(datetime(2023, 6, 4, 8, 00), datetime(2023, 6, 4, 8, 30))
    doctor3.add_available_time_slot(datetime(2023, 6, 4, 10, 00), datetime(2023, 6, 4, 10, 30))
    doctor3.add_available_time_slot(datetime(2023, 6, 4, 14, 00), datetime(2023, 6, 4, 14, 30))
    doctor3.add_available_time_slot(datetime(2023, 6, 5, 8, 30), datetime(2023, 6, 5, 9, 00))
    doctor3.add_available_time_slot(datetime(2023, 6, 5, 10, 30), datetime(2023, 6, 5, 11, 00))
    doctor3.add_available_time_slot(datetime(2023, 6, 5, 14, 30), datetime(2023, 6, 5, 15, 00))
    doctors.append(doctor3)

    qualification4 = Qualification("someOtherCertificate", conditions)
    doctor4 = Doctor("Larry Small", "male", [qualification4], languages)
    doctor4.add_available_time_slot(datetime(2023, 6, 4, 9, 00), datetime(2023, 6, 4, 9, 30))
    doctor4.add_available_time_slot(datetime(2023, 6, 4, 11, 00), datetime(2023, 6, 4, 11, 30))
    doctor4.add_available_time_slot(datetime(2023, 6, 4, 15, 30), datetime(2023, 6, 4, 16, 0))
    doctor4.add_available_time_slot(datetime(2023, 6, 5, 9, 30), datetime(2023, 6, 5, 10, 0))
    doctor4.add_available_time_slot(datetime(2023, 6, 5, 11, 30), datetime(2023, 6, 5, 12, 0))
    doctor4.add_available_time_slot(datetime(2023, 6, 5, 15, 30), datetime(2023, 6, 5, 16, 0))
    doctors.append(doctor4)

    return doctors


def create_test_patients(hospital_service):
    headache = Condition("headache")
    back_pain = Condition("back pain")
    copd = Condition("copd")
    cough = Condition("cough")
    existing_conditions = [headache, back_pain]
    languages = [Language.ENGLISH, Language.GERMAN]
    hospital_service.add_client("Jerry Seinfeld", datetime(1954, 4, 29), existing_conditions, languages)
    hospital_service.add_client("Cosmo Kramer", datetime(1949, 7, 24), [copd], languages)
    hospital_service.add_client("George Costanza", datetime(1959, 9, 23), existing_conditions, languages)
    hospital_service.add_client("Sharon Fredy", datetime(1989, 10, 28), [cough], languages)
