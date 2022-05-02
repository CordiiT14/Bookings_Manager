import unittest
from models.booking import Booking
from models.customer import Customer
from models.event import Event

class TestBooking(unittest.TestCase):

    def setUp(self):
        self.event_1 = Event("Loud Poets", "11 April 2022", "18:30", "Spoken Word", "Showcasing the top spoken word talent from Scotland and the UK! From laugh-out-loud funny, through the wonderfully surreal, to the thoughtful and emotional. Loud Poets continue to prove that Spoken Word has something for everyone.")
        self.customer_1 = Customer("Ella", "Bendall", "egbendall@mail.co.uk")
        self.customer_2 = Customer("Robbie", "Johnstone", "r_johnstone@gmail.com", "Customer has a nut allergy")
        
        self.booking_1 = Booking(self.event_1, self.customer_1)

    # def test_booking_id(self):
    #     self.assertEqual( None, self.booking_1.id)


    # # testing booking.event attributes

    # def test_event_name(self):
    #     self.assertEqual("Loud Poets", self.booking_1.event.event_title)

    # def test_event_date(self):
    #     self.assertEqual("11 April 2022", self.booking_1.event.date)

    # def test_event_time(self):
    #     self.assertEqual("18:30", self.booking_1.event.time)

    # def test_event_type(self):
    #     self.assertEqual("Spoken Word", self.booking_1.event.event_type)

    # def test_event_description(self):
    #     description = "Showcasing the top spoken word talent from Scotland and the UK! From laugh-out-loud funny, through the wonderfully surreal, to the thoughtful and emotional. Loud Poets continue to prove that Spoken Word has something for everyone." 
    #     self.assertEqual( description , self.booking_1.event.description)

    # def test_event_id(self):
    #     self.assertEqual( None, self.booking_1.event.id)

    # #testing booking.customer attributes

    # def test_customer_first_name(self):
    #     self.assertEqual("Ella", self.booking_1.customer.first_name)
        
    
    # def test_customer_last_name(self):
    #     self.assertEqual("Bendall", self.booking_1.customer.last_name)
        

    # def test_customer_email(self):
    #     self.assertEqual("egbendall@mail.co.uk", self.booking_1.customer.email)
    

    # def test_customer_notes_none(self):
    #     self.assertEqual( None, self.booking_1.customer.notes)


    # def test_customer_id(self):
    #     self.assertEqual( None, self.booking_1.customer.id)
 
    # def test_full_name_method(self):
    #     self.assertEqual("Ella Bendall", self.booking_1.customer.full_name(self.booking_1.customer))