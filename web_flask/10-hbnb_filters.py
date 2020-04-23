#!/usr/bin/python3
"""
 Starts an Flask web app
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ Display a predefined HTML page """
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exception):
    """ Close storage """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
