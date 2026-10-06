from persistence.in_memory_appointment_repository import InMemoryAppointmentRepository
from Services.appointment_service import AppointmentService
from presentation.cli import run

def main() -> None:
    repository = InMemoryAppointmentRepository()
    service = AppointmentService(repository)
    run(service)

if __name__ == '__main__':
    main()
