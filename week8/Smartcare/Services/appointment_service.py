from domain.appointment import Appointment
from domain.patient import Patient
from domain.practitioner import Practitioner
from repositories.appointment_repository import AppointmentRepository

class AppointmentService:
    def __init__(self, repository: AppointmentRepository) -> None:
        self._repository = repository

    def book_appointment(self, patient: Patient, practitioner: Practitioner, appointment_time: str) -> Appointment:
        appointment = Appointment(patient, practitioner, appointment_time)
        #Is practitioner busy?
        for existing in self._repository.get_all():
            if existing.is_active() and existing.get_practitioner().get_practitioner_id() == practitioner.get_practitioner_id() and existing.get_appointment_time() == appointment_time:
                raise ValueError(f"Practitioner is busy at {appointment_time}")
        self._repository.add(appointment)
        return appointment

    def get_active_appointments(self, patient: Patient) -> list[Appointment]:
        return [appointment for appointment in self._repository.get_all() if appointment.is_active() and appointment.get_patient().get_patient_id() == patient.get_patient_id()]

    def cancel_appointment(self, appointment: Appointment) -> None:
        appointment.cancel()
