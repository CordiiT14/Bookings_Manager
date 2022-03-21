from flask import render_template, redirect, request
from flask import Blueprint
from app import app
from models.event import Event

events_blueprint = Blueprint("events", __name__)

@events_blueprint.route('/events')
def view_all_events():
    pass

@events_blueprint.route('/events/new')
def new_events():
    pass

@events_blueprint.route('/events/<id>')
def view_event_details():
    pass

@events_blueprint.route('/events/edit')
def edit_event():
    pass