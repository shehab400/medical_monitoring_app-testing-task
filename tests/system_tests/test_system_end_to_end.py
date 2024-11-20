import unittest
from datetime import datetime
from app.monitoring_workflow import MedicalMonitoringApp

class TestSystemEndToEnd(unittest.TestCase):

    def setUp(self):
        # Initialize the MedicalMonitoringApp instance
        self.app = MedicalMonitoringApp()

    def test_end_to_end_workflow_with_alerts(self):
    # Simulate patient monitoring with abnormal values
        heart_rate = 200
        blood_pressure = 180
        oxygen_saturation = 70

        # Monitor the patient
        statuses = self.app.monitor_patient(heart_rate, blood_pressure, oxygen_saturation)

        # Check monitoring statuses
        expected_statuses = [
            "Alert: Heart Rate out of safe range!",
            "Alert: Blood Pressure out of safe range!",
            "Alert: Oxygen Saturation out of safe range!"
        ]
        self.assertEqual(statuses, expected_statuses)

        # Check generated alerts
        alerts = self.app.get_alerts()
        expected_alerts = [
            "Hospital contacted at 123-456-789.",
            "Ambulance dispatched to the location via 987-654-321."
        ]
        for alert in expected_alerts:
            self.assertIn(alert, alerts)



    def test_end_to_end_workflow_without_alerts(self):
        # Simulate patient monitoring with normal values
        heart_rate = 75
        blood_pressure = 110
        oxygen_saturation = 98

        # Monitor the patient
        statuses = self.app.monitor_patient(heart_rate, blood_pressure, oxygen_saturation)

        # Check monitoring statuses
        expected_statuses = [
            "Heart Rate is within safe range.",
            "Blood Pressure is within safe range.",
            "Oxygen Saturation is within safe range."
        ]
        self.assertEqual(statuses, expected_statuses)

        # Check no alerts
        alerts = self.app.get_alerts()
        self.assertEqual(alerts, [])






if __name__ == '__main__':
    unittest.main()
