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
