Act as a software architecture reviewer. Review this small SmartCare Python system against separation of concerns, cohesion, coupling and introductory SOLID principles. Identify concrete layer violations and dependency risks. Prefer the simplest refactoring that solves an observed problem. Do not introduce frameworks, microservices or patterns unless current requirements justify them.

appointment.py
from enum import Enum

from domain.patient import Patient
from domain.practitioner import Practitioner

class AppointmentStatus(Enum):
    BOOKED = "Booked"
    CANCELLED = "Cancelled"

class Appointment:
    def __init__(self, patient: Patient, practitioner: Practitioner, appointment_time: str) -> None:
        if not patient:
            raise ValueError("Patient is required")
        if not practitioner:
            raise ValueError("Practitioner is required")
        if not appointment_time:
            raise ValueError("appointment_time is required")

        self._patient = patient
        self._practitioner = practitioner
        self._appointment_time = appointment_time
        self._status = AppointmentStatus.BOOKED  # Rule: new appointment starts BOOKED

    def cancel(self) -> None:
        self._status = AppointmentStatus.CANCELLED

    def is_active(self) -> bool:
        return self._status != AppointmentStatus.CANCELLED

    def get_appointment_time(self) -> str:
        return self._appointment_time

    def get_status(self) -> AppointmentStatus:
        return self._status

    def get_patient(self) -> Patient:
        return self._patient

    def get_practitioner(self) -> Practitioner:
        return self._practitioner

patient.py
lass Patient:
    def __init__(self, name: str, patient_id: str) -> None:
        if not name:
            raise ValueError("Patient name cannot be empty")
        if not patient_id:
            raise ValueError("Patient id cannot be empty")
        self._name = name
        self._patient_id = patient_id

    def get_name(self) -> str:
        return self._name

    def get_patient_id(self) -> str:
        return self._patient_id

    def matches_id(self, patient_id) -> bool:
        return patient_id == self._patient_id

practitioner.py
class Practitioner:
    def __init__(self, name: str, practitioner_id: str, specialty: str) -> None:
        if not name:
            raise ValueError("Practitioners name cannot be empty")
        if not practitioner_id:
            raise ValueError("Practitioners id cannot be empty")
        if not specialty:
            raise ValueError("Practitioners specialty cannot be empty")
        self._name = name
        self._practitioner_id = practitioner_id
        self._specialty = specialty

    def get_name(self) -> str:
        return self._name

    def get_practitioner_id(self) -> str:
        return self._practitioner_id

    def get_specialty(self) -> str:
        return self._specialty

in_memory_appointment_repository.py
from domain.appointment import Appointment
from repositories.appointment_repository import AppointmentRepository

class InMemoryAppointmentRepository(AppointmentRepository):

    def __init__(self) -> None:
        self.appointments: list[Appointment] = []

    def add(self, appointment: Appointment) -> None:
        self.appointments.append(appointment)

    def get_all(self) -> list[Appointment]:
        return list(self.appointments)

cli.py
from domain.patient import Patient
from domain.practitioner import Practitioner
from Services.appointment_service import AppointmentService

def run(service: AppointmentService) -> None:
    print("=== SmartCare Demo ===")

    # Create patient
    patient_name = input("Enter patient name: ")
    patient_id = input("Enter patient id: ")
    patient = Patient(patient_name, patient_id)

    # Create practitioner
    practitioners_name = input("Enter practitioner's name: ")
    practitioners_id = input("Enter practitioner's id: ")
    practitioners_specialty = input("Enter practitioner's specialty: ")
    practitioner = Practitioner(practitioners_name, practitioners_id, practitioners_specialty)

    while True:
        user_input = input("book, view, cancel or quit?")
        if user_input == "book":
            # Book appointment
            time = input("Enter appointment time (e.g., 2024-07-20 10:00 AM): ")

            try:
                appointment = service.book_appointment(patient, practitioner, time)
                print("Appointment booked successfully!")
                print("Status:", appointment.get_status().value)
            except Exception as e:
                print("Failed to book appointment:", e)
        elif user_input == "view":
            active_appointments = service.get_active_appointments(patient)

            if not active_appointments:
                print("You have no appointments!")
                continue

            print("Your appointments:")

            for i, appointment in enumerate(active_appointments, start=1):
                print(f"{i}. {appointment.get_appointment_time()}" f" with {practitioner.get_name()}")


        elif user_input == "cancel":
            active_appointments = service.get_active_appointments(patient)

            if not active_appointments:
                print("You have no appointments to cancel!")
                continue

            print("Your appointments:")

            for i, appointment in enumerate(active_appointments, start=1):
                print(f"{i}. {appointment.get_appointment_time()}" f" with {appointment._practitioner.get_name()}")

            try:
                choice = int(input("Select appointment to cancel: "))

                if choice < 1 or choice > len(active_appointments):
                    print("Invalid choice. Please try again.")
                    continue

                appointment_to_cancel = active_appointments[choice - 1]

                service.cancel_appointment(appointment_to_cancel)

                print("Appointment cancelled.")
                print("Status:", appointment_to_cancel.get_status().value)

            except ValueError:
                print("Please enter a valid number")
        elif user_input == "quit":
            break
        else:
            print("Invalid input. Please try again.")

appointment_repository.py
from domain.appointment import Appointment

class AppointmentRepository:

    def add(self, appointment: Appointment) -> None:
        raise NotImplementedError

    def get_all(self) -> list[Appointment]:
        raise NotImplementedError

appointment_service.py
from domain.appointment import Appointment
from domain.patient import Patient
from domain.practitioner import Practitioner
from repositories.appointment_repository import AppointmentRepository

class AppointmentService:
    def __init__(self, repository: AppointmentRepository) -> None:
        self.repository = repository

    def book_appointment(self, patient: Patient, practitioner: Practitioner, appointment_time: str) -> Appointment:
        #Is practitioner busy?
        for appointment in self.repository.get_all():
            if appointment.is_active() and appointment.get_practitioner() is practitioner and appointment.get_appointment_time() == appointment_time:
                raise ValueError(f"Practitioner is busy at {appointment_time}")
        appointment = Appointment(patient, practitioner, appointment_time)
        self.repository.add(appointment)
        return appointment

    def get_active_appointments(self, patient: Patient) -> list[Appointment]:
        return [appointment for appointment in self.repository.get_all() if appointment.is_active() and appointment.get_patient() is patient]

    def cancel_appointment(self, appointment: Appointment) -> None:
        appointment.cancel()

and here is the structure
smartcare/
  main.py
  domain/
    __init__.py
    patient.py
    practitioner.py
    appointment.py
  services/
    __init__.py
    appointment_service.py
  repositories/
    __init__.py
    appointment_repository.py
  persistence/
    __init__.py
    in_memory_appointment_repository.py
  presentation/
    __init__.py
    cli.py