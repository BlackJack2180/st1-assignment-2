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

    def get_name(self) -> str:
        return self._name

    def get_practitioner_id(self) -> str:
        return self._practitioner_id

    def get_specialty(self) -> str:
        return self._specialty
