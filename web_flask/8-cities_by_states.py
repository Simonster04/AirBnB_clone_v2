#!/usr/bin/python3
"""
 Starts an Flask web app
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_state():
    """ Display a HTML page with all the states sorted by name"""
    states_list = sorted(storage.all('State').values(), key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states_list=states_list)


@app.teardown_appcontext
def teardown(exception):
    """ Close storage """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
