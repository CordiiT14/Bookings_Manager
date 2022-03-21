from flask import render_template, redirect, request
from flask import Blueprint
from models.customer import Customer
import repositories.customer_repository as customer_repository

customers_blueprint = Blueprint("customers", __name__)

@customers_blueprint.route('/customers')
def view_all_customer():
    customers = customer_repository.select_all()
    return render_template('/customers/index.html', title = 'Customers', all_customers = customers)

@customers_blueprint.route('/customers/new')
def new_customer():
    pass

@customers_blueprint.route('/customers/<id>')
def view_customer_details(id):
    customer = customer_repository.select(id)
    return render_template('/customers/view.html', title = customer.full_name(customer), customer = customer)

@customers_blueprint.route('/customers/edit')
def edit_customer():
    pass