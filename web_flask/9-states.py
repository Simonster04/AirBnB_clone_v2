#!/usr/bin/python3
"""
 Starts an Flask web app
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)



@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """ Display a HTML page with all the states and its cities sorted by name"""
    states = storage.all('State')
    if id is not None:
        id = 'State.' + id
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def teardown(exception):
    """ Close storage """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
