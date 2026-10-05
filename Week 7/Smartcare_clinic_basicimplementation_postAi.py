from enum import Enum


class Patient:
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
        self._appointments = []

    def get_name(self) -> str:
        return self._name

    def get_practitioner_id(self) -> str:
        return self._practitioner_id

    def get_specialty(self) -> str:
        return self._specialty

    def is_busy_at(self, time: str) -> bool:
        for appointment in self._appointments:
            if appointment.get_appointment_time() == time and appointment.is_active():
                return True
        return False

    def add_appointment(self, appointment) -> None:
        self._appointments.append(appointment)


# -----------------------------
# NEW ENUM + EXCEPTION
# -----------------------------

class AppointmentStatus(Enum):
    BOOKED = "Booked"
    CANCELLED = "Cancelled"


class InvalidStatusTransitionError(Exception):
    """Raised when an illegal appointment status change is attempted."""
    pass


# -----------------------------
# APPOINTMENT CLASS (UML‑APPROVED)
# -----------------------------

class Appointment:
    def __init__(self, patient: Patient, practitioner: Practitioner, appointment_time: str) -> None:
        # FR‑04: Validate required fields
        if not patient:
            raise ValueError("Patient is required")
        if not practitioner:
            raise ValueError("Practitioner is required")
        if not appointment_time:
            raise ValueError("Appointment time is required")

        # FR‑05 / NFR‑01: Practitioner must not be busy
        if practitioner.is_busy_at(appointment_time):
            raise ValueError(f"Practitioner is busy at {appointment_time}")

        self._patient = patient
        self._practitioner = practitioner
        self._appointment_time = appointment_time
        self._status = AppointmentStatus.BOOKED  # Rule: new appointment starts BOOKED

        # Register with practitioner (rule #3)
        practitioner.add_appointment(self)

    # UML operation
    def is_complete(self) -> bool:
        # Decision: UML says "is_complete() -> bool" but does not define meaning.
        # I interpret "complete" as "all required fields exist", which matches your comment.
        return (
            self._patient is not None and
            self._practitioner is not None and
            bool(self._appointment_time)
        )

    # UML operation
    def cancel(self) -> None:
        # FR‑08 / FR‑09 / US‑03: Only BOOKED → CANCELLED allowed
        if self._status == AppointmentStatus.CANCELLED:
            raise InvalidStatusTransitionError("Appointment is already cancelled")

        self._status = AppointmentStatus.CANCELLED

    # UML operation
    def is_active(self) -> bool:
        return self._status != AppointmentStatus.CANCELLED

    # UML operation
    def get_appointment_time(self) -> str:
        return self._appointment_time

    # Extra method required by business rule #7
    def get_status(self) -> AppointmentStatus:
        return self._status


# -----------------------------
# SIMPLE MAIN FOR BOOKING + CANCELLING
# -----------------------------

if __name__ == "__main__":
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
        user_input = input("book, cancel or quit?")
        if user_input == "book":
            # Book appointment
            time = input("Enter appointment time (e.g., 2024-07-20 10:00 AM): ")

            try:
                appointment = Appointment(patient, practitioner, time)
                print("Appointment booked successfully!")
                print("Status:", appointment.get_status().value)
            except Exception as e:
                print("Failed to book appointment:", e)
                exit()
        elif user_input == "cancel":
            # Optionally cancel
            do_cancel = input("Cancel this appointment? (yes/no): ").strip().lower()
            if do_cancel == "yes":
                try:
                    appointment.cancel()
                    print("Appointment cancelled.")
                    print("Status:", appointment.get_status().value)
                except InvalidStatusTransitionError as e:
                    print("Error:", e)
        elif user_input == "quit":
            break
        else:
            print("Invalid input. Please try again.")