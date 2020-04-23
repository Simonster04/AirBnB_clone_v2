#!/usr/bin/python3
"""
 Starts an Flask web app
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    """ Display a HTML page with all the states sorted by name"""
    states_list = sorted(storage.all('State').values(), key=lambda x: x.name)
    return render_template('7-states_list.html', states_list=states_list)


@app.teardown_appcontext
def teardown(exception):
    """ Close storage """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
