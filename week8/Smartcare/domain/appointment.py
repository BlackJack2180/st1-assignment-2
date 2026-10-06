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
