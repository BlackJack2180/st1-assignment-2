Below is the **full, copy‑paste‑ready file** with your **Patient**, **Practitioner**, and the **new AppointmentStatus enum**, **InvalidStatusTransitionError**, and the **correct Appointment class** implemented exactly according to the approved SmartCare UML and business rules.

I also updated `main` so you can **book and cancel appointments** interactively, but I kept it minimal and avoided any forbidden features.

I explain all design decisions **after the code**, exactly as you requested.

---

# ✅ **FULL FILE — COPY & PASTE**

```python
from enum import Enum


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

    # Book appointment
    time = input("Enter appointment time (e.g., 2024-07-20 10:00 AM): ")

    try:
        appointment = Appointment(patient, practitioner, time)
        print("Appointment booked successfully!")
        print("Status:", appointment.get_status().value)
    except Exception as e:
        print("Failed to book appointment:", e)
        exit()

    # Optionally cancel
    do_cancel = input("Cancel this appointment? (yes/no): ").strip().lower()
    if do_cancel == "yes":
        try:
            appointment.cancel()
            print("Appointment cancelled.")
            print("Status:", appointment.get_status().value)
        except InvalidStatusTransitionError as e:
            print("Error:", e)
```

---

# ✅ **DESIGN DECISIONS NOT VISIBLE IN UML (EXPLANATIONS)**

### **1. Why `is_complete()` checks for non‑None fields**
The UML only says:

> is_complete() -> bool

No definition is provided.  
Your earlier comment in the skeleton said:

> Return true if Patient, Practitioner and time are all present

So I implemented exactly that.  
This is a **UML‑inferred behaviour**, not explicitly defined.

---

### **2. Why `get_status()` exists**
The UML does **not** list `get_status()`, but your business rule #7 requires:

> Status must not be changeable directly from outside the class; cancel() is the only way it changes. Provide a read-only get_status() method.

Therefore, I added it.

---

### **3. Why status is stored as a private attribute**
UML says:

> Attributes (private): patient, practitioner, appointment_time, status

So `_status` is private.  
This prevents external mutation and enforces rule #7.

---

### **4. Why the constructor registers the appointment with the practitioner**
UML does not show this, but your business rule #3 requires:

> A new appointment starts as BOOKED and registers itself with the practitioner using practitioner.add_appointment(self).

So I added that call.

---

### **5. Why no “completed”, “no‑show”, or “reschedule” logic exists**
Your constraints explicitly forbid adding extra statuses or behaviours.

---

### **6. Why no printing or input inside Appointment**
Your constraints forbid UI logic inside domain classes.

---

### **7. Why the enum uses string values**
The UML does not specify the underlying type.  
Using `"Booked"` and `"Cancelled"` matches your requirement:

> exactly two values, BOOKED ("Booked") and CANCELLED ("Cancelled")

---

If you want next steps, I can help you implement:

- AppointmentRepository  
- SchedulingService  
- Conflict detection with durations  
- Practitioner availability rules  
- UML for Patient and Practitioner  
- Unit tests for Appointment  

Just tell me what direction you want to explore next.