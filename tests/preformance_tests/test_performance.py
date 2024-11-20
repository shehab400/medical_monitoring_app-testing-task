import time
import random
import sys
import os
from datetime import datetime

# Add the parent directory of the 'app' module to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, parent_dir)

from app.monitoring_workflow import MedicalMonitoringApp

class PerformanceTest:
    def __init__(self, app):
        self.app = app

    def measure_time(self, operation, *args):
        """Measure execution time of a given operation"""
        start_time = time.time()
        result = operation(*args)
        end_time = time.time()
        execution_time = end_time - start_time
        return result, execution_time

    def test_monitoring(self, iterations=1000):
        """Test the monitoring function multiple times"""
        monitoring_times = []
        for _ in range(iterations):
            heart_rate = random.randint(50, 150)
            blood_pressure = random.randint(70, 180)
            oxygen_saturation = random.randint(85, 100)
            _, exec_time = self.measure_time(self.app.monitor_patient, heart_rate, blood_pressure, oxygen_saturation)
            monitoring_times.append(exec_time)
        return monitoring_times

    def test_logging(self, iterations=1000):
        """Test the logging functions multiple times"""
        biosignal_times = []
        alert_times = []
        timestamp = datetime.now().isoformat()
        for _ in range(iterations):
            biosignal_data = {
                "heart_rate": random.randint(50, 150),
                "oxygen_saturation": random.randint(85, 100),
                "blood_pressure": f"{random.randint(70, 180)}/{random.randint(40, 120)}"
            }
            _, exec_time = self.measure_time(self.app.logger.log_biosignal, timestamp, biosignal_data)
            biosignal_times.append(exec_time)

            alert_message = "Test alert message"
            _, exec_time = self.measure_time(self.app.logger.log_alert, timestamp, alert_message)
            alert_times.append(exec_time)
        return biosignal_times, alert_times

    def print_performance(self, iterations=1000):
        monitoring_times = self.test_monitoring(iterations)
        biosignal_times, alert_times = self.test_logging(iterations)

        print(f"Monitoring execution times:")
        print(f"Total time: {sum(monitoring_times):.6f}s, Average time: {sum(monitoring_times)/iterations:.6f}s")
        print(f"Max time: {max(monitoring_times):.6f}s, Min time: {min(monitoring_times):.6f}s\n")

        print(f"Biosignal logging execution times:")
        print(f"Total time: {sum(biosignal_times):.6f}s, Average time: {sum(biosignal_times)/iterations:.6f}s")
        print(f"Max time: {max(biosignal_times):.6f}s, Min time: {min(biosignal_times):.6f}s\n")

        print(f"Alert logging execution times:")
        print(f"Total time: {sum(alert_times):.6f}s, Average time: {sum(alert_times)/iterations:.6f}s")
        print(f"Max time: {max(alert_times):.6f}s, Min time: {min(alert_times):.6f}s\n")

if __name__ == "__main__":
    app = MedicalMonitoringApp()
    performance_test = PerformanceTest(app)
    performance_test.print_performance(iterations=1000)