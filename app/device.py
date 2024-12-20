from app.biosignals import HeartRate, BloodPressure, OxygenSaturation

class WearableDevice:
    """Simulates the wearable device."""
    def __init__(self):
        self.heart_rate = HeartRate()
        self.blood_pressure = BloodPressure()
        self.oxygen_saturation = OxygenSaturation()

    def read_signals(self, heart_rate, blood_pressure, oxygen_saturation):
        if not isinstance(heart_rate, int):
            raise TypeError("Heart rate must be an integer.")
        if not isinstance(blood_pressure, int):
            raise TypeError("Blood pressure must be an integer.")
        if not isinstance(oxygen_saturation, int):
            raise TypeError("Oxygen saturation must be an integer.")
        
        hr_status = self.heart_rate.update_value(heart_rate)
        bp_status = self.blood_pressure.update_value(blood_pressure)
        ox_status = self.oxygen_saturation.update_value(oxygen_saturation)
        return [hr_status, bp_status, ox_status]