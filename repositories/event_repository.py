from db.run_sql import run_sql

from models.event import Event

def save(event):
    sql = "INSERT INTO events (event_title, date, time, event_type, description) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [event.event_title, event.date, event.time, event.event_type, event.description]
    results = run_sql(sql, values)
    id = results[0]['id']
    event.id = id
    return event 

def delete_all():
    sql = "DELETE FROM events"
    run_sql(sql)
    return

def select_all():
    events = []

    sql = "SELECT * FROM events"
    results = run_sql(sql)

    for row in results:
        event = Event(row['event_title'], row['date'], row['time'], row['event_type'], row['description'], row ['id'] )
        events.append(event)
    return events

def select(id):
    event = None

    sql = "SELECT * FROM events WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]

    if results is not None:
        event = Event(results['event_title'], results['date'], results['time'], results['event_type'], results['description'], results['id'])
    return event 

def update(event):
    sql = "UPDATE events SET (event_title, date, time, event_type, description) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [event.event_title, event.date, event.time, event.event_type, event.description, event.id]
    run_sql(sql, values)

def delete(id):
    pass