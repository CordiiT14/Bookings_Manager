from flask import render_template, redirect, request
from flask import Blueprint
from app import app
from models.customer import Customer

customers_blueprint = Blueprint("customers", __name__)