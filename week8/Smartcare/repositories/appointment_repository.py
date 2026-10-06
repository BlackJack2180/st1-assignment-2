from domain.appointment import Appointment

class AppointmentRepository:

    def add(self, appointment: Appointment) -> None:
        raise NotImplementedError

    def get_all(self) -> list[Appointment]:
        raise NotImplementedError
