import unittest
import os
import json
from datetime import datetime
from app.data_logger import DataLogger

class TestDataLoggerIntegration(unittest.TestCase):

    def setUp(self):
        # Set up temporary log files for testing
        self.log_file = "test_biosignal_logs.json"
        self.alert_file = "test_alerts.json"
        self.logger = DataLogger(log_file=self.log_file, alert_file=self.alert_file)

    def tearDown(self):
        # Clean up the temporary log files after each test
        if os.path.exists(self.log_file):
            os.remove(self.log_file)
        if os.path.exists(self.alert_file):
            os.remove(self.alert_file)

    def test_log_biosignal(self):
        # Arrange
        timestamp = datetime.now().isoformat()
        biosignal_data = {
            "heart_rate": 75,
            "blood_pressure": 120,
            "oxygen_saturation": 98,
            "statuses": [
                "Heart Rate is within safe range.",
                "Blood Pressure is within safe range.",
                "Oxygen Saturation is within safe range."
            ]
        }

        # Act
        self.logger.log_biosignal(timestamp, biosignal_data)

        # Assert
        with open(self.log_file, "r") as f:
            logs = json.load(f)
            self.assertEqual(len(logs), 1)
            self.assertEqual(logs[0]["timestamp"], timestamp)
            self.assertEqual(logs[0]["data"], biosignal_data)

    def test_log_alert(self):
        # Arrange
        timestamp = datetime.now().isoformat()
        alert_message = "Heart rate exceeds safe threshold!"

        # Act
        self.logger.log_alert(timestamp, alert_message)

        # Assert
        with open(self.alert_file, "r") as f:
            alerts = json.load(f)
            self.assertEqual(len(alerts), 1)
            self.assertEqual(alerts[0]["timestamp"], timestamp)
            self.assertEqual(alerts[0]["alert"], alert_message)

    def test_get_logs(self):
        # Arrange
        timestamp = datetime.now().isoformat()
        biosignal_data = {
            "heart_rate": 75,
            "blood_pressure": 120,
            "oxygen_saturation": 98,
            "statuses": [
                "Heart Rate is within safe range.",
                "Blood Pressure is within safe range.",
                "Oxygen Saturation is within safe range."
            ]
        }
        alert_message = "Heart rate exceeds safe threshold!"

        # Act
        self.logger.log_biosignal(timestamp, biosignal_data)
        self.logger.log_alert(timestamp, alert_message)
        biosignal_logs, alert_logs = self.logger.get_logs()

        # Assert
        self.assertEqual(len(biosignal_logs), 1)
        self.assertEqual(biosignal_logs[0]["timestamp"], timestamp)
        self.assertEqual(biosignal_logs[0]["data"], biosignal_data)

        self.assertEqual(len(alert_logs), 1)
        self.assertEqual(alert_logs[0]["timestamp"], timestamp)
        self.assertEqual(alert_logs[0]["alert"], alert_message)

    def test_invalid_log_biosignal(self):
        # Arrange
        timestamp = datetime.now().isoformat()
        biosignal_data = "Invalid data type"  # Invalid type, should be a dictionary

        # Act & Assert
        with self.assertRaises(TypeError):
            self.logger.log_biosignal(timestamp, biosignal_data)

    def test_invalid_log_alert(self):
        # Arrange
        timestamp = datetime.now().isoformat()
        alert_message = 12345  # Invalid type, should be a string

        # Act & Assert
        with self.assertRaises(TypeError):
            self.logger.log_alert(timestamp, alert_message)

if __name__ == '__main__':
    unittest.main()