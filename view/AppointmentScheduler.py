import TestData
from view import UiHelper
from view.AppointmentSchedulerAction import AppointmentSchedulerAction
from service.HospitalService import HospitalService


class AppointmentScheduler:
    def __init__(self):
        hospital = TestData.create_test_hospital()
        self.hospital_service = HospitalService(hospital)
        TestData.create_test_patients(self.hospital_service)
        self.start_application()

    def start_application(self):
        selected_action = self.list_actions()
        while selected_action:
            if selected_action == 0:
                quit()
            elif selected_action == 1:
                pass
            elif selected_action == 2:
                self.add_client()
            elif selected_action == 3:
                self.list_clients()
            elif selected_action == 4:
                self.book_appointment()
            elif selected_action == 5:
                self.print_hospital_information()
            elif selected_action == 6:
                self.list_appointments()
            else:
                print(f'Action {selected_action} is not supported')
            selected_action = self.list_actions()

    @staticmethod
    def list_actions():
        UiHelper.print_header('Available Actions')
        print(f'{[action for action in AppointmentSchedulerAction]}')
        return int(input('Please select an action by entering the corresponding number: '))

    def add_client(self):
        UiHelper.print_header('Add client')
        name = input('Please enter the client\'s full name: ')
        date_of_birth = UiHelper.parse_date(input('Please enter the client\'s date of birth(DD-MM-YYYY): '))
        existing_conditions = UiHelper.parse_conditions(
            input('Please enter the client\'s existing conditions (comma separated): '))
        languages = UiHelper.parse_languages(input('Please enter the client\'s languages in CAPS (comma separated): '))
        self.hospital_service.add_client(name, date_of_birth, existing_conditions, languages)

    def list_clients(self):
        UiHelper.print_header('List clients')
        if self.hospital_service.clients:
            print(str(self.hospital_service.clients))
        else:
            print('No clients registered yet')

    def book_appointment(self):
        self.list_clients()
        selected_client = UiHelper.parse_client(
            input('Please enter the full name of the client you want to book an appointment for: '),
            self.hospital_service.clients)
        date_time_from = UiHelper.parse_date_time(input('Please enter the start datetime of your appointment: '))
        date_time_to = UiHelper.parse_date_time(input('Please enter the end datetime of your appointment: '))
        available_time_slots = self.hospital_service.get_available_slots(selected_client, date_time_from, date_time_to)
        print(available_time_slots)
        selected_time_slot_index = int(input('Please select the number of the timeslot to book an appointment: '))
        selected_time_slot = available_time_slots[selected_time_slot_index]
        self.hospital_service.book_appointment(selected_client, selected_time_slot)

    def print_hospital_information(self):
        UiHelper.print_header('Hospital Information')
        print(self.hospital_service.get_hospital_information())

    def list_appointments(self):
        UiHelper.print_header('List Appointments')
        if self.hospital_service.appointment_requests:
            print(self.hospital_service.appointment_requests)
        else:
            print("No appointments created yet")
