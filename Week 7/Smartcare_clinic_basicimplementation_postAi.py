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
            raise ValueError("Appointment time is required")

        if practitioner.is_busy_at(appointment_time):
            raise ValueError(f"Practitioner is busy at {appointment_time}")

        self._patient = patient
        self._practitioner = practitioner
        self._appointment_time = appointment_time
        self._status = AppointmentStatus.BOOKED  # Rule: new appointment starts BOOKED

        practitioner.add_appointment(self)

    def cancel(self) -> None:
        self._status = AppointmentStatus.CANCELLED

    def is_active(self) -> bool:
        return self._status != AppointmentStatus.CANCELLED

    def get_appointment_time(self) -> str:
        return self._appointment_time

    def get_status(self) -> AppointmentStatus:
        return self._status

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

    appointments = []

    while True:
        user_input = input("book, view, cancel or quit?")
        if user_input == "book":
            # Book appointment
            time = input("Enter appointment time (e.g., 2024-07-20 10:00 AM): ")

            try:
                appointment = Appointment(patient, practitioner, time)
                appointments.append(appointment)
                print("Appointment booked successfully!")
                print("Status:", appointment.get_status().value)
            except Exception as e:
                print("Failed to book appointment:", e)
        elif user_input == "view":
            active_appointments = [
                appointment for appointment in appointments if appointment.is_active()
            ]

            if not active_appointments:
                print("You have no appointments!")
                continue

            print("Your appointments:")

            for i, appointment in enumerate(active_appointments, start=1):
                print(f"{i}. {appointment.get_appointment_time()}" f" with {practitioner.get_name()}")


        elif user_input == "cancel":
            active_appointments = [
                appointment for appointment in appointments if appointment.is_active()
            ]

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

                appointment_to_cancel.cancel()

                print("Appointment cancelled.")
                print("Status:", appointment_to_cancel.get_status().value)

            except ValueError:
                print("Please enter a valid number")
        elif user_input == "quit":
            break
        else:
            print("Invalid input. Please try again.")
