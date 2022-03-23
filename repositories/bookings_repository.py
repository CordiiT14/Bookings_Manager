from db.run_sql import run_sql
from models.booking import Booking
from models.customer import Customer
from models.event import Event

import repositories.event_repository as event_repository
import repositories.customer_repository as customer_repository


def save(booking):
    sql = "INSERT INTO bookings (event_id, customer_id) VALUES (%s, %s) RETURNING id"
    values = [booking.event.id, booking.customer.id]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return booking 


def update(booking):
    sql = "UPDATE bookings SET (event_id, customer_id) = (%s, %s) WHERE id = %s"
    values = [booking.event.id, booking.customer.id, booking.id]
    run_sql(sql, values)

#used in the console to clear seed data - not in program
def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)
    return

#Below currently being used. Would use for furture extention to list all bookings.
def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for rows in results:
        event = event_repository.select(rows['event_id'])
        customer = customer_repository.select(rows['customer_id'])
        booking = Booking(event, customer, rows['id'])
        bookings.append(booking)
    return bookings
