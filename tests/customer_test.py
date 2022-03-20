import unittest
from models.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer_1 = Customer("Ella", "Bendall", "egbendall@mail.co.uk")
        self.customer_2 = Customer("Robbie", "Johnstone", "r_johnstone@gmail.com", "Customer has a nut allergy")
        
    def test_customer_first_name(self):
        self.assertEqual("Ella", self.customer_1.first_name)
        self.assertEqual ("Robbie", self.customer_2.first_name)