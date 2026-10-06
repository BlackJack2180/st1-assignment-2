from domain.appointment import Appointment
from repositories.appointment_repository import AppointmentRepository

class InMemoryAppointmentRepository(AppointmentRepository):

    def __init__(self) -> None:
        self._appointments: list[Appointment] = []

    def add(self, appointment: Appointment) -> None:
        self._appointments.append(appointment)

    def get_all(self) -> list[Appointment]:
        return list(self._appointments)
