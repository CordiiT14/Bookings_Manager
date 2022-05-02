import unittest
from models.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer_1 = Customer("Ella", "Bendall", "egbendall@mail.co.uk")
        self.customer_2 = Customer("Robbie", "Johnstone", "r_johnstone@gmail.com", "Customer has a nut allergy")
        
    # def test_customer_first_name(self):
    #     self.assertEqual("Ella", self.customer_1.first_name)
    #     self.assertEqual ("Robbie", self.customer_2.first_name)
    
    # def test_customer_last_name(self):
    #     self.assertEqual("Bendall", self.customer_1.last_name)
    #     self.assertEqual("Johnstone", self.customer_2.last_name)

    # def test_customer_email(self):
    #     self.assertEqual("egbendall@mail.co.uk", self.customer_1.email)
    #     self.assertEqual("r_johnstone@gmail.com", self.customer_2.email)

    # def test_customer_notes_none(self):
    #     self.assertEqual( None, self.customer_1.notes)

    # def test_customer_note(self):
    #     self.assertEqual( "Customer has a nut allergy", self.customer_2.notes)

    # def test_customer_id(self):
    #     self.assertEqual( None, self.customer_1.id)
    #     self.assertEqual(None, self.customer_2.id)

    # def test_full_name_method(self):
    #     self.assertEqual("Robbie Johnstone", self.customer_2.full_name(self.customer_2))