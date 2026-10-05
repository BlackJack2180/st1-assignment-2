Act as a Python pair programmer. Implement only the Appointment class from the approved SmartCare UML. Use type hints and an AppointmentStatus enum. Cancelled appointments remain as objects. Do not add database, UI, notification or service classes. Protect status transitions and explain any decision not directly visible in the UML.

APPROVED UML - Appointment
Attributes (private): patient, practitioner, appointment_time (str), status (AppointmentStatus)
Operations: is_complete() -> bool, cancel() -> None, is_active() -> bool, get_appointment_time() -> str

ALSO IMPLEMENT ONLY: an AppointmentStatus enum with exactly two values, BOOKED ("Booked") and CANCELLED ("Cancelled"), and one custom exception for an illegal status change (suggested name: InvalidStatusTransitionError).

ALREADY EXISTING (do not rewrite, do not import, assume they are defined above in the same file):
- Patient: get_name(), get_patient_id(), matches_id(patient_id)
- Practitioner: get_name(), get_practitioner_id(), get_specialty(), is_busy_at(time: str) -> bool, add_appointment(appointment) -> None

RELATIONSHIPS
- Each appointment is for exactly 1 Patient and with exactly 1 Practitioner. The appointment holds references to those objects, not copies of names.

BUSINESS RULES
1. FR-04: Creating an appointment must fail with ValueError if the patient, practitioner or time is missing.
2. FR-05 / NFR-01: Creating an appointment must fail with ValueError and a clear message if practitioner.is_busy_at(time) is True.
3. A new appointment starts as BOOKED and registers itself with the practitioner using practitioner.add_appointment(self).
4. FR-08 / FR-09 / US-03: cancel() changes the status from BOOKED to CANCELLED. The object is never deleted.
5. Cancelling an appointment that is already cancelled must raise InvalidStatusTransitionError.
6. is_active() returns True only when the status is not CANCELLED.
7. Status must not be changeable directly from outside the class; cancel() is the only way it changes. Provide a read-only get_status() method.

CONSTRAINTS
- Use only the Python standard library (enum). No other imports.
- Do not add statuses such as completed or no-show, and no rescheduling, rebooking, reports, saving to files, input() or print() calls.
- Keep it as small and simple as possible.
- For every decision that is not visible in the UML above, say so and explain it.

Inegrate your code directly into my code and sent a full thing back that can be copy and pasted
class Patient:
    def __init__(self, name: str, patient_id: str) -> None:
        self._name = name
        self._patient_id = patient_id
        if not name:
            raise ValueError("Patient name cannot be empty")
        if not patient_id:
            raise ValueError("Patient id cannot be empty")
        self._name = name
        self._patient_id = patient_id

    def get_name(self) -> str:
        #return patients name
        return self._name

    def get_patient_id(self) -> str:
        return self._patient_id
        #return patients id
        return self._patient_id

    def matches_id(self, patient_id) -> bool:
        #returns true if the user searched for this patients id
        if patient_id == self._patient_id:
            return True
        else:
            return False


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
        #return true if an active appointment exists at this time
        for appointment in self._appointments:
            if appointment.get_appointment_time() == time and appointment.is_active():
                return True
        return False

    def add_appointment(self, appointment: Appointment) -> None:
        self._appointments.append(appointment)

class Appointment:
    def __init__(self, patient, practitioner, appointment_time, status="Booked"):
        self._patient = patient
        self._practitioner = practitioner
        self._appointment_time = appointment_time
        self._status = status

    def is_complete(self):
        #Return true if Patient, Practitioner and time are all present
        pass

    def cancel(self):
        #set the status to cancelled and keep the record
        pass

    def is_active(self):
        #return true if the status is not set to cancelled
        pass

    def get_appointment_time(self):
        return self._appointment_time

if __name__ == "__main__":
    patient_name = input("Enter patient name:")
    patient_id = input("Enter patient id: ")
    patient = Patient(patient_name, patient_id)
    print("Patient: ", patient.get_name(), patient.get_patient_id())

    practitioners_name = input("Enter practitioners name:")
    practitioners_id = input("Enter practitioners id: ")
    practitioners_specialty = input("Enter practitioners specialty: ")
    practitioner = Practitioner(practitioners_name, practitioners_id, practitioners_specialty)
    print("Practitioner:: ", practitioner.get_name(), practitioner.get_practitioner_id(), practitioner.get_specialty())


    #patient = Patient("Jane Doe", "p001")
    #practitioner = Practitioner("Dr Ridley")
    #appointment = Appointment(patient, practitioner, "2024-07-20 2:00 PM")

    #print("Skeleton objects created: Patient, Practitioner, Appointment")
    #print("Patient: ", patient.get_name())
    #print("Practitioner: ", practitioner.get_name())
    #print("Appointment class:", type(appointment).__name__)

Your welcome to change main just to implement tha ability to book and cancel appointments