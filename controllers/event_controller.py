from flask import render_template, redirect, request
from flask import Blueprint
from models.event import Event
import repositories.event_repository as event_repository

events_blueprint = Blueprint("events", __name__)

@events_blueprint.route('/events')
def view_all_events():
    events = event_repository.select_all()
    return render_template('/events/index.html', title = 'All Events', all_events = events)

@events_blueprint.route('/events/new')
def new_events():
    return render_template('/events/new.html', title = 'Add Event')

@events_blueprint.route('/events/<id>')
def view_event_details(id):
    event = event_repository.select(id)
    return render_template('/events/view.html', title=event.event_title, event = event)

@events_blueprint.route('/events/edit')
def edit_event():
    pass