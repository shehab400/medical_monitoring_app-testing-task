import os
import sys
import logging

# Add the parent directory of the 'app' module to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
class Biosignal:
    """Base class for biosignals."""
    def __init__(self, name, safe_range):
        self.name = name
        self.safe_range = safe_range
        self.value = None

    def update_value(self, value):
       
        self.value = value
        return self.check_threshold()

    def check_threshold(self):
        if not (self.safe_range[0] <= self.value <= self.safe_range[1]):
            return f"Alert: {self.name} out of safe range!"
        return f"{self.name} is within safe range."

class HeartRate(Biosignal):
    """Heart rate signal class."""
    def __init__(self):
        super().__init__("Heart Rate", (60, 100))

class BloodPressure(Biosignal):
    """Blood pressure signal class."""
    def __init__(self):
        super().__init__("Blood Pressure", (80, 120))

class OxygenSaturation(Biosignal):
    """Oxygen saturation signal class."""
    def __init__(self):
        super().__init__("Oxygen Saturation", (95, 100))
