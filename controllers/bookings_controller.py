from flask import render_template, redirect, request
from flask import Blueprint
from models.booking import Booking
from repositories.bookings_repository import customer

import repositories.customer_repository as customer_repository
import repositories.event_repository as event_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route('/bookings/<id>')
def book_event(id):
    event = event_repository.select(id)
    customers = customer_repository.select_all()
    return render_template('/bookings/book_event.html', title = 'New Booking', event = event, all_customers = customers)