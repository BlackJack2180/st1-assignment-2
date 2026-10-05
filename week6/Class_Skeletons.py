class Patient:
    def __init__(self, name, patient_id):
        self._name = name
        self._patient_id = patient_id

    def get_name(self):
        #return patients name
        return self._name

    def matches_id(self, patient_id):
        #returns true if the user searched for this patients id
        pass

class Practitioner:
    def __init__(self, name):
        self._name = name
        self._appointments = []

    def get_name(self):
        return self._name

    def is_busy_at(self, time):
        #return true if an active appointment exists at this time
        pass

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

if __name__ == "__main__":
    patient = Patient("Jane Doe", "p001")
    practitioner = Practitioner("Dr Ridley")
    appointment = Appointment(patient, practitioner, "2024-07-20 2:00 PM")

    print("Skeleton objects created: Patient, Practitioner, Appointment")
    print("Patient: ", patient.get_name())
    print("Practitioner: ", practitioner.get_name())
    print("Appointment class:", type(appointment).__name__)
