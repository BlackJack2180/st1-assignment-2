class Patient:
    def __init__(self, name: str, patient_id: str) -> None:
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
