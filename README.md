# python_project_bookings_manager

##Project Brief

### Theatre

A local theatre has asked you to build a piece of software to help them to manage customers, and register customers for events.

#### MVP

- The app should allow the theatre to create and edit Customers
- The app should allow the theatre to create and edit Events
- The app should allow the theatre to book customers on specific events
- The app should show a list of all upcoming events
- The app should show all customers that are booked in for a particular event

#### Extensions

- The app could allow the Theatre to delete customers
- The app 
- The app could allow the Theatre to archive old events, these should be shown in an archive and no longer display in the upcoming events list.


### Programme Set Up

- Clone project to your local repository
- Create database bookings_manager:
> create db bookings_manager
- Run the following in your terminal from the root to create database tables:
> psql -d bookings_manager -f db/bookings_manager.sql
- Run the console file to populate the tables with seed data:
> python3 console.py
