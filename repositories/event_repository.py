from db.run_sql import run_sql

from models.event import Event

def save(event):
    sql = "INSERT INTO events (event_title, date, time, event_type, description) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [event.event_title, event.date, event.time, event.event_type, event.description]
    results = run_sql(sql, values)
    event.id = results[0]['id']
    return event 

def delete_all():
    sql = "DELETE FROM events"
    run_sql(sql)