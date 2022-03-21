from flask import render_template, redirect, request, url_for
from flask import Blueprint
from models.booking import Booking
import repositories.bookings_repository as booking_repository

import repositories.customer_repository as customer_repository
import repositories.event_repository as event_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route('/bookings/<id>')
def book_event(id):
    event = event_repository.select(id)
    customers = customer_repository.select_all()
    return render_template('/bookings/book_event.html', title = 'New Booking', event = event, all_customers = customers)

@bookings_blueprint.route('/bookings/new', methods=['POST'])
def add_booking():
    event_id = request.form['event_id']
    customer_id = request.form['customer_id']
    event = event_repository.select(event_id)
    customer = customer_repository.select(customer_id)
    booking = Booking(event, customer)
    booking_repository.save(booking)
    return redirect(url_for('events.view_event_details', id = event_id))