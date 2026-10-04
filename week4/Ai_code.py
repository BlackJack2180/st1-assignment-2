appointments = []  # This will store all appointment records


def add_appointment(patient, practitioner, time):
    """Store a new appointment in the appointments list."""

    # Basic validation to help beginners avoid mistakes
    if not patient:
        print("Error: Patient name cannot be empty.")
        return
    if not practitioner:
        print("Error: Practitioner name cannot be empty.")
        return
    if not time:
        print("Error: Appointment time cannot be empty.")
        return

    appointment = {
        "patient": patient,
        "practitioner": practitioner,
        "time": time
    }

    appointments.append(appointment)
    print("Appointment added successfully!")


def show_appointments():
    """Display all stored appointments."""
    if not appointments:
        print("No appointments found.")
        return

    print("\nCurrent Appointments:")
    for appt in appointments:
        print(f"Patient: {appt['patient']} | Practitioner: {appt['practitioner']} | Time: {appt['time']}")

#Improvement from me (Following code not made by ai)
#Code that allows the user to interact with the system (add/view appointments)
def input_appointments():
    patient = input("Patient: ")
    practitioner = input("Practitioner: ")
    time = input("Appointment time: ")
    add_appointment(patient, practitioner, time)
    show_appointments()
    input_appointments()

input_appointments()