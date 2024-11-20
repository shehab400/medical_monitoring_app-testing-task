from app.emergency_service import EmergencyService
import unittest


class Test_emergency_service(unittest.TestCase):



    def test_contact_hospital(self):
        # Arrange: Prepare input values
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
    
        
        


if __name__ == '__main__':
    unittest.main()


    def test_dispatch_ambulance(self):
       pass
        
        
        


if __name__ == '__main__':
    unittest.main()
