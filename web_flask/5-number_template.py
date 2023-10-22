#!/usr/bin/python3
<<<<<<< HEAD
"""script that starts a Flask web application"""

from flask import Flask, render_template
=======
""" Script that runs an app with Flask framework """
from flask import Flask, render_template


>>>>>>> dd948381d6da4095df99c2d43111eceeecf1e0da
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
<<<<<<< HEAD
    """/: displays Hello HBNB!"""
=======
    """ Function called with / route """
>>>>>>> dd948381d6da4095df99c2d43111eceeecf1e0da
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
<<<<<<< HEAD
    """prints HBNB when /hbnb is called"""
=======
    """ Function called with /hbnb route """
>>>>>>> dd948381d6da4095df99c2d43111eceeecf1e0da
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
<<<<<<< HEAD
def c_is_fun(text):
    """prints text when /c is called"""
    return "C " + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is_cool'):
    """prints text when /python is called"""
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def is_n_number(n):
    """/number/<n>: display n is a number only if n is an integer"""
    return "{:d} is a number".format(n)
=======
def c_text(text):
    """ Function called with /c/<text> route """
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """ Function called with /python/<text> route """
    if text is not 'is cool':
        text = text.replace('_', ' ')
    return 'Python %s' % text


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Function called with /number/<n> route """
    return "%d is a number" % n
>>>>>>> dd948381d6da4095df99c2d43111eceeecf1e0da


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
<<<<<<< HEAD
    """displays a HTML page only if n is an integer"""
    return render_template('5-number.html', value=n)
=======
    """ Function called with /number_template/<n> route """
    return render_template('5-number.html', number=n)
>>>>>>> dd948381d6da4095df99c2d43111eceeecf1e0da


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
