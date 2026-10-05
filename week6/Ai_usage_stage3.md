Below is a **requirement‑supported domain model** for SmartCare, based *only* on confirmed requirements.  
Every class, attribute, operation and relationship cites its supporting IDs.

---

# **1. Suggested Classes**

### **Table: Classes, Types, Attributes, Operations, Supporting IDs**

| **Class** | **Type** | **Attributes** | **Operations** | **Supporting IDs** |
|----------|----------|----------------|----------------|--------------------|
| **Patient** | Domain concept | patientId (FR‑02, US‑04, US‑05), name (FR‑01), *no other attributes are supported by requirements* | registerPatient() (FR‑01), findById() (FR‑02, US‑04, US‑05) | FR‑01, FR‑02, US‑04, US‑05 |
| **Practitioner** | Domain concept | practitionerId (FR‑03), name (brief: clinic has practitioners) | *No operations explicitly required* | FR‑03, NFR‑01 |
| **Appointment** | Domain concept | appointmentId (needed for history display – FR‑06, FR‑09), time (FR‑03), status (FR‑07, FR‑09), patientId (FR‑03, NFR‑01), practitionerId (FR‑03, NFR‑01) | createAppointment() (FR‑03), cancelAppointment() (FR‑08, FR‑09), checkDuplicate() (FR‑05, NFR‑01) | FR‑03, FR‑04, FR‑05, FR‑06, FR‑07, FR‑08, FR‑09, NFR‑01 |
| **AppointmentRepository** | Technical component (storage) | storedAppointments (NFR‑02) | save(), findAll(), findByPractitionerAndTime(), updateStatus() | NFR‑02, NFR‑03, NFR‑04 |
| **PatientRepository** | Technical component (storage) | storedPatients (NFR‑02) | save(), findById() | NFR‑02, NFR‑03, NFR‑04 |
| **BookingService** | Technical component (business logic) | *No attributes required* | bookAppointment() (FR‑03, FR‑04, FR‑05), validateInputs() (FR‑04), preventDuplicate() (FR‑05, NFR‑01) | NFR‑03, NFR‑04, FR‑03, FR‑04, FR‑05 |
| **CancellationService** | Technical component (business logic) | *No attributes required* | cancel() (FR‑08), updateStatusToCancelled() (FR‑09) | FR‑08, FR‑09, NFR‑03, NFR‑04 |

---

# **2. Suggested Relationships**

### **Table: Relationships, Multiplicity, Supporting IDs**

| **From** | **To** | **Relationship Type** | **Multiplicity** | **Supporting IDs** |
|----------|--------|------------------------|------------------|--------------------|
| **Patient** | Appointment | A patient has many appointments | 1 patient : 0..* appointments | FR‑03, FR‑06, FR‑09, NFR‑01 |
| **Appointment** | Patient | Each appointment refers to exactly one patient | 1 appointment : 1 patient | FR‑03, FR‑04, NFR‑01 |
| **Practitioner** | Appointment | A practitioner has many appointments | 1 practitioner : 0..* appointments | FR‑03, FR‑05, FR‑06, NFR‑01 |
| **Appointment** | Practitioner | Each appointment refers to exactly one practitioner | 1 appointment : 1 practitioner | FR‑03, FR‑04, NFR‑01 |
| **AppointmentRepository** | Appointment | Repository stores many appointments | 1 repository : 0..* appointments | NFR‑02 |
| **PatientRepository** | Patient | Repository stores many patients | 1 repository : 0..* patients | NFR‑02 |
| **BookingService** | AppointmentRepository | Service uses repository to store and query appointments | 1 service : 1 repository | NFR‑03, NFR‑04 |
| **CancellationService** | AppointmentRepository | Service updates appointment status via repository | 1 service : 1 repository | NFR‑03, NFR‑04 |

---

# **3. Unsupported Ideas (Needs Client Validation)**

These concepts were considered but **no confirmed requirement supports them**, so they are *not included* in the model:

- **Patient contact details** (phone, email, address)  
  *No requirement mentions them.*

- **Appointment duration or end time**  
  *Requirements only mention a single appointment time.*

- **Practitioner working hours or availability schedule**  
  *FR‑10 was provisional and is not confirmed.*

- **Audit trail or cancellation reason**  
  *Not in confirmed requirements.*

- **User accounts, roles, authentication**  
  *Not mentioned in any confirmed requirement.*

- **Reporting classes**  
  *FR‑11 was provisional and not confirmed.*

---

# **4. Two Questions to Test Your Understanding**

1. **Why does the Appointment class require a status attribute, and which requirement(s) justify it?**  
2. **What requirement prevents us from adding practitioner working hours to the domain model?**

If you want, I can also produce a **diagram‑style UML version** of this model.