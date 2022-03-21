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
    return render_template('customers/new.html', title='Add New Customer')

@customers_blueprint.route('/customers/new', methods=['POST'])
def add_new_customer():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    notes = request.form['notes']
    customer = Customer(first_name, last_name, email, notes)
    customer = customer_repository.save(customer)
    return redirect('/customers')

@customers_blueprint.route('/customers/<id>')
def view_customer_details(id):
    customer = customer_repository.select(id)
    return render_template('/customers/view.html', title = customer.full_name(customer), customer = customer)

@customers_blueprint.route('/customers/edit')
def edit_customer():

    return render_template('/customers/edit.html', title= 'Update Details')