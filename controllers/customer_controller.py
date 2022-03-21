from flask import render_template, redirect, request
from flask import Blueprint
from app import app
from models.customer import Customer

customers_blueprint = Blueprint("customers", __name__)

@customers_blueprint.route('/customers')
def view_all_customer():
    pass

@customers_blueprint.route('/customers/new')
def new_customer():
    pass

@customers_blueprint.route('/customers/<id>')
def view_event_details():
    pass

@customers_blueprint.route('/customers/edit')
def edit_event():
    pass