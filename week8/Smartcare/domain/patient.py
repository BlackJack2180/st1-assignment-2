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
