import unittest
from unittest.mock import patch
from datetime import datetime
from app.monitoring_workflow import MedicalMonitoringApp

class TestMedicalMonitoringApp(unittest.TestCase):

    def setUp(self):
        # Arrange: Initialize the MedicalMonitoringApp instance
        self.app = MedicalMonitoringApp()
        self.timestamp = datetime.now().isoformat()

    @patch('app.monitoring_workflow.WearableDevice.read_signals')
    @patch('app.monitoring_workflow.DataLogger.log_biosignal')
    @patch('app.monitoring_workflow.DataLogger.log_alert')
    @patch('app.monitoring_workflow.EmergencyService.contact_hospital')
    @patch('app.monitoring_workflow.EmergencyService.dispatch_ambulance')
    def test_monitor_patient_with_alerts(self, mock_dispatch_ambulance, mock_contact_hospital, mock_log_alert, mock_log_biosignal, mock_read_signals):
        # Arrange: Mock the return values
        mock_read_signals.return_value = ["Alert: Heart Rate out of safe range!", "Blood Pressure is within safe range.", "Alert: Oxygen Saturation out of safe range!"]
        mock_contact_hospital.return_value = "Hospital contacted at 123-456-789."
        mock_dispatch_ambulance.return_value = "Ambulance dispatched to 987-654-321."

        # Act: Monitor the patient
        statuses = self.app.monitor_patient(heart_rate=200, blood_pressure=120, oxygen_saturation=70)

        # Assert: Check if the statuses and alerts are as expected
        self.assertEqual(statuses, ["Alert: Heart Rate out of safe range!", "Blood Pressure is within safe range.", "Alert: Oxygen Saturation out of safe range!"])
        self.assertIn("Hospital contacted at 123-456-789.", self.app.get_alerts())
        self.assertIn("Ambulance dispatched to 987-654-321.", self.app.get_alerts())
        mock_log_biosignal.assert_called_once()
        mock_log_alert.assert_called()

    @patch('app.monitoring_workflow.WearableDevice.read_signals')
    @patch('app.monitoring_workflow.DataLogger.log_biosignal')
    def test_monitor_patient_without_alerts(self, mock_log_biosignal, mock_read_signals):
        # Arrange: Mock the return values
        mock_read_signals.return_value = ["Heart Rate is within safe range.", "Blood Pressure is within safe range.", "Oxygen Saturation is within safe range."]

        # Act: Monitor the patient
        statuses = self.app.monitor_patient(heart_rate=75, blood_pressure=120, oxygen_saturation=98)

        # Assert: Check if the statuses are as expected and no alerts are generated
        self.assertEqual(statuses, ["Heart Rate is within safe range.", "Blood Pressure is within safe range.", "Oxygen Saturation is within safe range."])
        self.assertEqual(self.app.get_alerts(), [])
        mock_log_biosignal.assert_called_once()
        
    @patch('app.monitoring_workflow.EmergencyService.contact_hospital')
    @patch('app.monitoring_workflow.EmergencyService.dispatch_ambulance')
    @patch('app.monitoring_workflow.DataLogger.log_alert')
    def test_handle_emergency(self, mock_log_alert, mock_dispatch_ambulance, mock_contact_hospital):
        # Arrange: Mock the return values
        mock_contact_hospital.return_value = "Hospital contacted at 123-456-789."
        mock_dispatch_ambulance.return_value = "Ambulance dispatched to 987-654-321."

        # Act: Handle the emergency
        self.app.handle_emergency(self.timestamp)

        # Assert: Check if the alerts are as expected
        self.assertIn("Hospital contacted at 123-456-789.", self.app.get_alerts())
        self.assertIn("Ambulance dispatched to 987-654-321.", self.app.get_alerts())
        mock_log_alert.assert_any_call(self.timestamp, "Hospital contacted at 123-456-789.")
        mock_log_alert.assert_any_call(self.timestamp, "Ambulance dispatched to 987-654-321.")

    def test_invalid_monitor_patient(self):
        # Act & Assert
        with self.assertRaises(TypeError):
            self.app.monitor_patient(heart_rate="invalid", blood_pressure=120, oxygen_saturation=98)
        with self.assertRaises(TypeError):
            self.app.monitor_patient(heart_rate=75, blood_pressure="invalid", oxygen_saturation=98)
        with self.assertRaises(TypeError):
            self.app.monitor_patient(heart_rate=75, blood_pressure=120, oxygen_saturation="invalid")

if __name__ == '__main__':
    unittest.main()