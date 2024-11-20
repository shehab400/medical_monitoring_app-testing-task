from app.biosignals import HeartRate, BloodPressure, OxygenSaturation
import unittest

class TestBiosignal(unittest.TestCase):

    def setUp(self):
        # Arrange: Initialize Biosignals instance
        self.HeartRte = HeartRate()
        self.BloodPressure = BloodPressure()
        self.OxygenSaturation = OxygenSaturation()

    def test_update_values(self):
        # Test values
        HeartRateValue = "Heart Rate is within safe range."
        BloodPressureValue = "Blood Pressure is within safe range."
        OxygenSaturationValue = "Oxygen Saturation is within safe range."

        # Act: Update the values
        Heart_result = self.HeartRte.update_value(60)
        Blood_result = self.BloodPressure.update_value(80)
        Oxygen_result = self.OxygenSaturation.update_value(95)

        # Assert: Check if the results are as expected
        self.assertEqual(Heart_result, HeartRateValue)
        self.assertEqual(Blood_result, BloodPressureValue)
        self.assertEqual(Oxygen_result, OxygenSaturationValue)

    def test_check_threshold(self):
        # Test values out of range
        TestLessRange = 30
        heart_out_range = "Alert: Heart Rate out of safe range!"
        blood_out_range = "Alert: Blood Pressure out of safe range!"
        oxygen_out_range = "Alert: Oxygen Saturation out of safe range!"
        TestInRange = 100
        heart_in_range = "Heart Rate is within safe range."
        blood_in_range = "Blood Pressure is within safe range."
        oxygen_in_range = "Oxygen Saturation is within safe range."
        TestMoreRange = 200
        
        # Test negative values
        TestNegative = -10
        heart_negative = "Alert: Heart Rate out of safe range!"
        blood_negative = "Alert: Blood Pressure out of safe range!"
        oxygen_negative = "Alert: Oxygen Saturation out of safe range!"


        # Act: Update the values and check thresholds
        Heart_result_less = self.HeartRte.update_value(TestLessRange)
        Heart_result_in = self.HeartRte.update_value(TestInRange)
        Heart_result_more = self.HeartRte.update_value(TestMoreRange)
        Heart_result_negative = self.HeartRte.update_value(TestNegative)
        # blood pressure
        blood_Pressure_less = self.BloodPressure.update_value(TestLessRange)
        blood_Pressure_in = self.BloodPressure.update_value(TestInRange)
        blood_Pressure_more = self.BloodPressure.update_value(TestMoreRange)
        blood_Pressure_negative = self.BloodPressure.update_value(TestNegative)
        #oxygen saturation
        oxygen_saturation_less = self.OxygenSaturation.update_value(TestLessRange)
        oxygen_saturation_in = self.OxygenSaturation.update_value(TestInRange)
        oxygen_saturation_more = self.OxygenSaturation.update_value(TestMoreRange)
        oxygen_saturation_negative = self.OxygenSaturation.update_value(TestNegative)
        

        # Assert: Check if the results are as expected
        self.assertEqual(Heart_result_less, heart_out_range)
        self.assertEqual(Heart_result_in, heart_in_range)
        self.assertEqual(Heart_result_more, heart_out_range)
        self.assertEqual(blood_Pressure_less, blood_out_range)
        self.assertEqual(blood_Pressure_in, blood_in_range)
        self.assertEqual(blood_Pressure_more, blood_out_range)
        self.assertEqual(oxygen_saturation_less, oxygen_out_range)
        self.assertEqual(oxygen_saturation_in, oxygen_in_range)
        self.assertEqual(oxygen_saturation_more, oxygen_out_range)
        self.assertEqual(Heart_result_negative, heart_negative)
        self.assertEqual(blood_Pressure_negative, blood_negative)
        self.assertEqual(oxygen_saturation_negative, oxygen_negative)
        
        
        


if __name__ == '__main__':
    unittest.main()
