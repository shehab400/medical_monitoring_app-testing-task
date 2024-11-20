from app.biosignals import HeartRate, BloodPressure, OxygenSaturation
import unittest

class TestBiosignal(unittest.TestCase):

    def setUp(self):
        # Arrange: Initialize the Calculator instance
        self.HeartRte = HeartRate()
        self.BloodPressure = BloodPressure()
        self.OxygenSaturation = OxygenSaturation()

    def test_update_values(self):
        # Arrange: Prepare input values
        pass
        
        # # Act: Perform the addition
        # result=self.calculator.add(a,b)
        # # Assert: Check if the result is as expected
        # self.assertEqual(result,expected_result)

    def test_check_threshold(self):
        # Test values out of range
        TestLessRange = 30
        ResultLessRange = "Alert: Heart Rate out of safe range!"
        ResultLessRangeBlood = "Alert: Blood Pressure out of safe range!"
        ResultLessRangeOxygen = "Alert: Oxygen Saturation out of safe range!"
        TestInRange = 100
        ResultInRange = "Heart Rate is within safe range."
        ResultInRangeBlood = "Blood Pressure is within safe range."
        ResultInRangeOxygen = "Oxygen Saturation is within safe range."
        TestMoreRange = 200
        ResultMoreRange = "Alert: Heart Rate out of safe range!"
        ResultMoreRangeBlood = "Alert: Blood Pressure out of safe range!"
        ResultMoreRangeOxygen = "Alert: Oxygen Saturation out of safe range!"

        # Act: Update the values and check thresholds
        Heart_result_less = self.HeartRte.update_value(TestLessRange)
        Heart_result_in = self.HeartRte.update_value(TestInRange)
        Heart_result_more = self.HeartRte.update_value(TestMoreRange)
        # blood pressure
        blood_Pressure_less = self.BloodPressure.update_value(TestLessRange)
        blood_Pressure_in = self.BloodPressure.update_value(TestInRange)
        blood_Pressure_more = self.BloodPressure.update_value(TestMoreRange)
        #oxygen saturation
        oxygen_saturation_less = self.OxygenSaturation.update_value(TestLessRange)
        oxygen_saturation_in = self.OxygenSaturation.update_value(TestInRange)
        oxygen_saturation_more = self.OxygenSaturation.update_value(TestMoreRange)
        

        # Assert: Check if the results are as expected
        self.assertEqual(Heart_result_less, ResultLessRange)
        self.assertEqual(Heart_result_in, ResultInRange)
        self.assertEqual(Heart_result_more, ResultMoreRange)
        self.assertEqual(blood_Pressure_less, ResultLessRangeBlood)
        self.assertEqual(blood_Pressure_in, ResultInRangeBlood)
        self.assertEqual(blood_Pressure_more, ResultMoreRangeBlood)
        self.assertEqual(oxygen_saturation_less, ResultLessRangeOxygen)
        self.assertEqual(oxygen_saturation_in, ResultInRangeOxygen)
        self.assertEqual(oxygen_saturation_more, ResultMoreRangeOxygen)
        
        
        


if __name__ == '__main__':
    unittest.main()
