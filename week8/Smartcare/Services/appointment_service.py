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
