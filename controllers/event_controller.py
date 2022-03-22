from flask import render_template, redirect, request
from flask import Blueprint
from models.event import Event
import repositories.event_repository as event_repository

events_blueprint = Blueprint("events", __name__)

@events_blueprint.route('/events')
def view_all_events():
    events = event_repository.select_all_active()
    return render_template('/events/index.html', title = 'All Events', all_events = events)

@events_blueprint.route('/events/new')
def new_events():
    return render_template('/events/new.html', title = 'Add Event')

@events_blueprint.route('/events/new', methods=['POST'])
def add_new_event():
    event_title = request.form['event_title']
    date = request.form['date']
    time = request.form['time']
    event_type = request.form['event_type']
    description = request.form['description']
    event = Event(event_title, date, time, event_type, description)
    event = event_repository.save(event)
    return render_template('events/view.html', title = event.event_title, event = event)

@events_blueprint.route('/events/<id>')
def view_event_details(id):
    event = event_repository.select(id)
    bookings = event_repository.customers_list_for_event(id)
    return render_template('/events/view.html', title=event.event_title, event = event, all_bookings = bookings)

@events_blueprint.route('/events/<id>/edit')
def edit_event(id):
    event = event_repository.select(id)
    return render_template('/events/edit.html', title = "Edit Event", event = event)

@events_blueprint.route('/events/<id>/edit', methods=['POST'])
def update_event(id):
    event_title = request.form['event_title']
    date = request.form['date']
    time = request.form['time']
    event_type = request.form['event_type']
    description = request.form['description']
    event = Event(event_title, date, time, event_type, description, id)
    event_repository.update(event)
    return render_template('/events/view.html', title = event.event_title, event = event)

@events_blueprint.route('/events/archived')
def all_archived_events():
    archived = event_repository.select_archived()
    active = event_repository.select_all_active()
    return render_template('/events/archived.html', title = "Archived Events", archived_events = archived, active_events = active) 

@events_blueprint.route('/events/archived', methods=['POST'])
def archive_event():
    event_id = request.form['event_id']
    event = event_repository.select(event_id)
    event.archive_event(event)
    event_repository.update(event)
    return redirect('/events/archived')