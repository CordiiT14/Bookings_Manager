from flask import render_template, redirect, request
from flask import Blueprint
from app import app
from models.event import Event

events_blueprint = Blueprint("events", __name__)