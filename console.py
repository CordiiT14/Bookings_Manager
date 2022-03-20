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

event_1 = Event("Loud Poets", "11 April 2022", "18:30", "Spoken Word", "Showcasing the top spoken word talent from Scotland and the UK! From laugh-out-loud funny, through the wonderfully surreal, to the thoughtful and emotional. Loud Poets continue to prove that Spoken Word has something for everyone.")
event_repository.save(event_1)


customer_1 = Customer("Sabrina", "Morales", "s.morales@emails.uk", "Customer is a wheelchair user")
customer_repository.save(customer_1)
customer_2 = Customer("Robbie", "Johnstone", "r.m.johnstone@mail.com")
customer_repository.save(customer_2)



booking_1 = Booking(event_1, customer_1)
bookings_repository.save(booking_1)

# customers = customer_repository.select_all()
# for customer in customers:
#     print(customer.__dict__)

print(customer_repository.select(customer_1.id).__dict__)
customer_1.notes = None

customer_repository.update(customer_1)
print(customer_1.__dict__)
