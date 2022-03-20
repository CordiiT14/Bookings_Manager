from curses import REPORT_MOUSE_POSITION
import pdb
from models.event import Event
from models.customer import Customer
from models.booking import Booking

import repositories.bookings_repository as bookings_repository
import repositories.event_repository as event_repository
import repositories.customer_repository as customer_repository

event_repository.delete_all()
customer_repository.delete_all()
bookings_repository.delete_all()

# EVENT REPOSITORY TESTING

event_1 = Event("Loud Poets", "11 April 2022", "18:30", "Spoken Word", "Showcasing the top spoken word talent from Scotland and the UK! From laugh-out-loud funny, through the wonderfully surreal, to the thoughtful and emotional. Loud Poets continue to prove that Spoken Word has something for everyone.")
event_repository.save(event_1)
event_2 = Event("The Man in the Submarine", "8 April 2022", "19:00", "Theatre", "A new play from L20 director, producer and playwright Laila Noble that tells the story of a man in a submarine and the care surrounding him as his hold on the world begins to loosen.")
event_repository.save(event_2)

# events = event_repository.select_all()

# for event in events:
#     print(event.__dict__)

# event_repository.delete(event_2.id)

# events = event_repository.select_all()

# for event in events:
#     print(event.__dict__)

# print(event_repository.select(event_2.id).__dict__)

# event_2.time = "19:30"

# event_repository.update(event_2)

# print(event_repository.select(event_2.id).__dict__)


# CUSTOMER REPOSITORY TESTING
customer_1 = Customer("Sabrina", "Morales", "s.morales@emails.uk", "Customer is a wheelchair user")
customer_repository.save(customer_1)
customer_2 = Customer("Robbie", "Johnstone", "r.m.johnstone@mail.com")
customer_repository.save(customer_2)

# print(customer_repository.select(customer_1.id).__dict__)
# customer_1.notes = None

# customer_repository.update(customer_1)
# print(customer_1.__dict__)

# customer_repository.delete(customer_1.id)

# customers = customer_repository.select_all()
# for customer in customers:
#     print(customer.__dict__)


# TESTING OF BOOKING REPOSITORY FUNCTIONS
booking_1 = Booking(event_1, customer_1)
bookings_repository.save(booking_1)

bookings_repository.delete(booking_1.id)
