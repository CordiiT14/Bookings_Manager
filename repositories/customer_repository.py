from db.run_sql import run_sql
from models.customer import Customer
from models.event import Event

def save(customer):
    sql = "INSERT INTO customers (first_name, last_name, email, notes) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [customer.first_name, customer.last_name, customer.email, customer.notes]
    results = run_sql(sql, values)
    customer.id = results[0]['id']
    return customer 

def delete_all():
    sql = "DELETE FROM customers"
    run_sql(sql)
    return 

def select_all():
    customers = []

    sql = "SELECT * FROM customers"
    results = run_sql(sql)

    for row in results:
        customer = Customer(row['first_name'], row['last_name'], row['email'], row['notes'], row['id'])
        customers.append(customer)
    
    return customers 

def select(id):
    customer = None

    sql = "SELECT * FROM customers WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]

    if results is not None:
        customer = Customer(results['first_name'], results['last_name'], results['email'],results['notes'], id)
    return customer


def update(customer):
    sql = "UPDATE customers SET (first_name, last_name, email, notes) = (%s, %s, %s, %s) WHERE id = %s"
    values = [customer.first_name, customer.last_name, customer.email, customer.notes, customer.id]
    run_sql(sql, values)
    

def delete(id):
    sql = "DELETE FROM customers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def list_booked_events(id):
    events = []

    sql = "SELECT events.* FROM events INNER JOIN bookings ON bookings.event_id = events.id WHERE bookings.customer_id = %s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        event = Event(row['event_title'], row['date'], row['time'], row['event_type'], row['description'], row['id'])
        events.append(event)
    return events 
