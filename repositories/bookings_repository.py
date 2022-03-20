from db.run_sql import run_sql
from models.booking import Booking
from models.customer import Customer
from models.event import Event

def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)
    return

def save(booking):
    sql = "INSERT INTO bookings (event_id, customer_id) VALUES (%s, %s) RETURNING id"
    values = [booking.event.id, booking.customer.id]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return booking 

def select(id):
    pass

def update(booking):
    pass

def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)