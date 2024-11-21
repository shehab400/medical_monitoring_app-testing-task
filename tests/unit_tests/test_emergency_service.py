from app.emergency_service import EmergencyService
import unittest


class Test_emergency_service(unittest.TestCase):



    def test_contact_hospital(self):
        # Arrange: Prepare input values
        hospital_contact = "123-456-7890"
        expected_result = "Hospital contacted at 123-456-7890."
        self.emergency_service = EmergencyService(hospital_contact, "987-654-3210")
        # Act: Call the contact_hospital method
        result = self.emergency_service.contact_hospital()
    
        # Assert: Check if the result is as expected
        self.assertEqual(result, expected_result)
        

    def test_dispatch_ambulance(self):
        ambulance_contact = "987-654-3210"
        hospital_contact = "123-456-7890"
        expected_result = "Ambulance dispatched to the location via 987-654-3210."
        self.emergency_service = EmergencyService(hospital_contact, ambulance_contact)
        # Act: Call the contact_hospital method
        result = self.emergency_service.dispatch_ambulance()
        # Assert: Check if the result is as expected
        self.assertEqual(result, expected_result)
    
    def test_invalid_hospital_contact(self):
        # Arrange: Prepare invalid input values
        hospital_contact = 1234567890  # Invalid type, should be a string
        with self.assertRaises(TypeError):
            self.emergency_service = EmergencyService(hospital_contact, "987-654-3210")

    def test_invalid_ambulance_contact(self):
        # Arrange: Prepare invalid input values
        ambulance_contact = 9876543210  # Invalid type, should be a string
        with self.assertRaises(TypeError):
            self.emergency_service = EmergencyService("123-456-7890", ambulance_contact)
        
if __name__ == '__main__':
    unittest.main()