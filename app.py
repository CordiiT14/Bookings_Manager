from flask import Flask, render_template

from controllers.event_controller import events_blueprint
from controllers.customer_controller import customers_blueprint
from controllers.bookings_controller import bookings_blueprint

app = Flask(__name__)

app.register_blueprint(events_blueprint)
app.register_blueprint(customers_blueprint)
app.register_blueprint(bookings_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)