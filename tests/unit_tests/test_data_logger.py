import unittest
from datetime import datetime
from app.data_logger import DataLogger
import os
import json

class TestDataLogger(unittest.TestCase):

    def setUp(self):
        # Arrange: Initialize the DataLogger instance with test files
        self.log_file = "test_biosignal_logs.json"
        self.alert_file = "test_alerts.json"
        self.logger = DataLogger(log_file=self.log_file, alert_file=self.alert_file)
        self.timestamp = datetime.now().isoformat()

    def tearDown(self):
        # Clean up: Remove test files after each test
        if os.path.exists(self.log_file):
            os.remove(self.log_file)
        if os.path.exists(self.alert_file):
            os.remove(self.alert_file)

    def test_log_biosignal(self):
        # Arrange: Prepare biosignal data
        biosignal_data = {
            "heart_rate": 75,
            "oxygen_saturation": 98,
            "blood_pressure": "120/80"
        }
        expected_entry = {
            "timestamp": self.timestamp,
            "data": biosignal_data
        }

        # Act: Log the biosignal data
        self.logger.log_biosignal(self.timestamp, biosignal_data)

        # Assert: Check if the data is logged correctly
        with open(self.log_file, "r") as f:
            logs = json.load(f)
            self.assertIn(expected_entry, logs)

    def test_log_alert(self):
        # Arrange: Prepare alert message
        alert_message = "Heart rate exceeds safe threshold!"
        expected_entry = {
            "timestamp": self.timestamp,
            "alert": alert_message
        }

        # Act: Log the alert message
        self.logger.log_alert(self.timestamp, alert_message)

        # Assert: Check if the alert is logged correctly
        with open(self.alert_file, "r") as f:
            alerts = json.load(f)
            self.assertIn(expected_entry, alerts)

    def test_get_logs(self):
        # Arrange: Prepare biosignal data and alert message
        biosignal_data = {
            "heart_rate": 75,
            "oxygen_saturation": 98,
            "blood_pressure": "120/80"
        }
        alert_message = "Heart rate exceeds safe threshold!"
        self.logger.log_biosignal(self.timestamp, biosignal_data)
        self.logger.log_alert(self.timestamp, alert_message)

        # Act: Retrieve the logs
        biosignal_logs, alert_logs = self.logger.get_logs()

        # Assert: Check if the logs are retrieved correctly
        self.assertEqual(len(biosignal_logs), 1)
        self.assertEqual(len(alert_logs), 1)
        self.assertEqual(biosignal_logs[0]["data"], biosignal_data)
        self.assertEqual(alert_logs[0]["alert"], alert_message)

    def test_invalid_log_biosignal(self):
        # Arrange
        biosignal_data = "Invalid data type"  # Invalid type, should be a dictionary

        # Act & Assert
        with self.assertRaises(TypeError):
            self.logger.log_biosignal(self.timestamp, biosignal_data)

    def test_invalid_log_alert(self):
        # Arrange
        alert_message = 12345  # Invalid type, should be a string

        # Act & Assert
        with self.assertRaises(TypeError):
            self.logger.log_alert(self.timestamp, alert_message)

if __name__ == '__main__':
    unittest.main()