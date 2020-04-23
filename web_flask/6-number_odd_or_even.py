#!/usr/bin/python3
"""
 Starts an Flask web app
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ Returns Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """ Returns “C ” followed by the value of text """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    """ Returns “Python ” followed by the value of text """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def num_route(n):
    """ Returns “n is a number” only if n is an integer """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """ Returns “n is a number” only if n is an integer """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_odd(n):
    """ Returns “n is a even|odd” only if n is an integer """
    if n % 2 == 0:
        text = 'even'
    else:
        text = 'odd'
    final = "{} is {}".format(n, text)
    return render_template('6-number_odd_or_even.html', n=final)


if __name__ == '__main__':
    app.run(host='0.0.0.0')