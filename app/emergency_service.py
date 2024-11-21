class EmergencyService:
    """Simulates contacting emergency services."""
    def __init__(self, hospital_contact, ambulance_contact):
        if not isinstance(hospital_contact, str):
            raise TypeError("Hospital contact must be a string.")
        if not isinstance(ambulance_contact, str):
            raise TypeError("Ambulance contact must be a string.")
        
        self.hospital_contact = hospital_contact
        self.ambulance_contact = ambulance_contact

    def contact_hospital(self):
        return f"Hospital contacted at {self.hospital_contact}."

    def dispatch_ambulance(self):
        return f"Ambulance dispatched to the location via {self.ambulance_contact}."