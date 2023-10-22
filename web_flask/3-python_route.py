#!/usr/bin/python3
<<<<<<< HEAD
"""script that starts a Flask web application"""

from flask import Flask
=======
""" Script that runs an app with Flask framework """
from flask import Flask


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
    """/hbnb: displays HBNB"""
=======
    """ Function called with /hbnb route """
>>>>>>> dd948381d6da4095df99c2d43111eceeecf1e0da
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
<<<<<<< HEAD
def c_is_fun(text):
    """/c/<text>: display C followed by the value of the text variable"""
    return "C " + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is_cool'):
    """
    /python/<text>: display Python followed by the value
    of the text variable
    """
    return "Python " + text.replace('_', ' ')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
>>>>>>> dd948381d6da4095df99c2d43111eceeecf1e0da
