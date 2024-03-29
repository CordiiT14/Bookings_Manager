from db.run_sql import run_sql

from models.event import Event
from models.customer import Customer

def save(event):
    sql = "INSERT INTO events (event_title, date, time, event_type, archive, description) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [event.event_title, event.date, event.time, event.event_type, event.archive, event.description]
    results = run_sql(sql, values)
    id = results[0]['id']
    event.id = id
    return event 

def select(id):
    event = None

    sql = "SELECT * FROM events WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]

    if results is not None:
        event = Event(results['event_title'], results['date'], results['time'], results['event_type'], results['description'], results['archive'], results['id'])
    return event 

def update(event):
    sql = "UPDATE events SET (event_title, date, time, event_type, description, archive) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [event.event_title, event.date, event.time, event.event_type, event.description, event.archive, event.id]
    run_sql(sql, values)

#extension

def customers_list_for_event(id):
    customers = []

    sql = "SELECT customers.* FROM customers INNER JOIN bookings ON bookings.customer_id = customers.id WHERE bookings.event_id = %s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        customer = Customer(row['first_name'], row['last_name'], row['email'], row['notes'], row['id'])
        customers.append(customer)
        
    return customers

def select_all_active():
    active_events =[]

    sql = "SELECT * FROM events WHERE archive = False"
    results = run_sql(sql)

    for row in results:
        event = Event(row['event_title'], row['date'], row['time'], row['event_type'], row['description'], row['archive'], row['id'] )
        active_events.append(event)
    return active_events

def select_archived():
    archived_events =[]

    sql = "SELECT * FROM events WHERE archive = True"
    results = run_sql(sql)

    for row in results:
        event = Event(row['event_title'], row['date'], row['time'], row['event_type'], row['description'], row['archive'], row['id'] )
        archived_events.append(event)
    return archived_events

#only used in console to clear seed data before repopulating - not in program
def delete_all():
    sql = "DELETE FROM events"
    run_sql(sql)
    return

#Currently not used within the program - replaced with the archiving functionality.
def delete(id):
    sql = "DELETE FROM events WHERE id = %s"
    values = [id]
    run_sql(sql, values)

#Replaced by select_all_active and select_archived
def select_all():
    events = []

    sql = "SELECT * FROM events"
    results = run_sql(sql)

    for row in results:
        event = Event(row['event_title'], row['date'], row['time'], row['event_type'], row['description'], row['archive'], row['id'] )
        events.append(event)
    return events