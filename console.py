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

# SEED DATA

event_1 = Event("Loud Poets", "11 April 2022", "18:30", "Spoken Word", "Showcasing the top spoken word talent from Scotland and the UK! From laugh-out-loud funny, through the wonderfully surreal, to the thoughtful and emotional. Loud Poets continue to prove that Spoken Word has something for everyone.")
event_repository.save(event_1)
event_2 = Event("The Man in the Submarine", "8 April 2022", "19:00", "Theatre", "A new play from L20 director, producer and playwright Laila Noble that tells the story of a man in a submarine and the care surrounding him as his hold on the world begins to loosen.")
event_repository.save(event_2)
event_3 = Event("Guid Crack: Spring Rising", "25 March 2022", "19:30", "Storytelling", "Gather round the digital campfire with guest storyteller Claire Hewitt to share tales from the North that celebrate light, life and hope returning as the Spring Equinox approaches and bird song fills the air. Stories and songs that like the swallows and cranes, know of no borders. This evening will be dedicated to the people of Ukraine and their rich folklore traditions so please bring a candle to light together at the beginning.")
event_repository.save(event_3)
event_4 = Event("Scott Gibson: Rejoice", "26 May 2022", "20:00", "Comedy", "Scott Gibson (Edinburgh Award Winner, Scottish Variety Award Winner, Chortle Nominee), Glasgow’s critically-acclaimed and award-winning son, is touring once again with a brand new hour of darkly comedic storytelling.")
event_repository.save(event_4)
event_5 = Event("007 Voices Of Bond", "5 Auguts 2022", "15:40", "Music", "Immerse yourself in the world of James Bond and the legendary voices that have accompanied six decades of the world’s most-famous spy. Features all the hits including Goldfinger, Skyfall, Diamonds Are Forever, Live and Let Die and many more. Brought to you by Maia Elsey and the multi award-winning cast of Night Owl Shows. ")
event_repository.save(event_5)
event_6 = Event("Is This a Dagger?", "28 August 2021", "11:30", "Theatre", "By the pricking of my thumb, something wicked this way comes. Andy Cannon returns to the Netherbow stage to tell Shakespeare’s classic, taking audiences on a thousand-year journey from fact to fiction and back again.")
event_repository.save(event_6)
event_6.archive_event(event_6)
event_repository.update(event_6)

customer_1 = Customer("Sabrina", "Morales", "s.morales@emails.uk", "Customer is a wheelchair user")
customer_repository.save(customer_1)
customer_2 = Customer("Robbie", "Johnstone", "r.m.johnstone@mail.com")
customer_repository.save(customer_2)
customer_3 = Customer("Elle", "Macdonald", "macdonald.elle@hotmail.com")
customer_repository.save(customer_3)
customer_4 = Customer("Josef", "Nolan", "jo-no@mail.de", "Partially sighted likes to sit in the front row")
customer_repository.save(customer_4)
customer_5 = Customer("Hannah", "Finlay", "finlay69@mail.co.uk")
customer_repository.save(customer_5)



booking_1 = Booking(event_1, customer_1)
bookings_repository.save(booking_1)
booking_2 = Booking(event_1, customer_2)
bookings_repository.save(booking_2)
booking_3 = Booking(event_2, customer_1)
bookings_repository.save(booking_3)



# -------EVENT REPOSITORY TESTING---------

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

# customer_list = event_repository.customers_list_for_event(event_1.id)

# for customer in customer_list:
#     print(customer.full_name(customer))
#     print(customer.notes)
#     print(customer.id)

# active = event_repository.select_all_active()

# for event in active:
#     print(event.__dict__)


# event_4.archive_event(event_4)

# event_repository.update(event_4)

# archived = event_repository.select_archived()

# for event in archived:
#     print(event.__dict__)



# --------CUSTOMER REPOSITORY TESTING--------------

# print(customer_repository.select(customer_1.id).__dict__)
# customer_1.notes = None

# customer_repository.update(customer_1)
# print(customer_1.__dict__)

# customer_repository.delete(customer_1.id)

# customers = customer_repository.select_all()
# for customer in customers:
#     print(customer.__dict__)

# events_list = customer_repository.list_booked_events(customer_1.id)

# for events in events_list:
#     print(events.event_title)
#     print(events.id)


# --------TESTING OF BOOKING REPOSITORY FUNCTIONS-------

# bookings_repository.delete(booking_1.id)

# booking_1.customer = customer_2

# bookings_repository.update(booking_1)

# bookings = bookings_repository.select_all()

# for booking in bookings:
#     print(booking.__dict__)

# print(bookings_repository.customer(booking_1).__dict__)
# print(bookings_repository.event(booking_1).__dict__)