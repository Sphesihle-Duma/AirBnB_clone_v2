#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """/: displays Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """prints HBNB when /hbnb is called"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
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


@app.route('/number/<int:n>', strict_slashes=False)
def is_n_number(n):
    """/number/<n>: display n is a number only if n is an integer"""
    return "{:d} is a number".format(n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
