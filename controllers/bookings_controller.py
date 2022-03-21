from flask import render_template, redirect, request
from flask import Blueprint
from models.booking import Booking

bookings_blueprint = Blueprint("bookings", __name__)