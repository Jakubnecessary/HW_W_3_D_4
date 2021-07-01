from flask import render_template, request, redirect
from app import app
from models.event_list import *
from models.event import *

@app.route('/events')
def index():
    return render_template('index.html', title="Homepage", events=events)

@app.route('/events', methods=['post'])
def add_event():
    event_date = request.form['date']
    event_name = request.form['event_name']
    number_of_guests = request.form['number_of_guests']
    room_loction = request.form['room_location']
    description = request.form['description']
    new_event = Event(event_date, event_name, number_of_guests, room_loction, description)
    add_new_event(new_event)
    return redirect('/events')
    
