from app.device import WearableDevice
import unittest

class TestDevice(unittest.TestCase):

    def setUp(self):
        # Arrange: Initialize the Calculator instance
        self.device = WearableDevice()


    def test_read_signals(self):
        # Test values out of range
        Results_less_list = ["Alert: Heart Rate out of safe range!", "Alert: Blood Pressure out of safe range!", "Alert: Oxygen Saturation out of safe range!"]
        Results_InRange_list = ["Heart Rate is within safe range.", "Blood Pressure is within safe range.", "Oxygen Saturation is within safe range."]
        Results_More_list = ["Alert: Heart Rate out of safe range!", "Alert: Blood Pressure out of safe range!", "Alert: Oxygen Saturation out of safe range!"]

        # Act: Update the values and check thresholds
        result_less = self.device.read_signals(30,30,30)
        result_in =  self.device.read_signals(100,100,100)
        result_more =  self.device.read_signals(200,200,200)
        # blood pressure
        

        # Assert: Check if the results are as expected
        self.assertEqual(result_less, Results_less_list)
        self.assertEqual(result_in, Results_InRange_list)
        self.assertEqual(result_more, Results_More_list)
        
        
        


if __name__ == '__main__':
    unittest.main()