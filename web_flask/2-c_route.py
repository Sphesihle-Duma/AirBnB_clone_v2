#!/usr/bin/python3
<<<<<<< HEAD
"""script that starts a Flask web application"""

from flask import Flask
=======
""" Creates a flask app that handles three route """
from flask import Flask

>>>>>>> dd948381d6da4095df99c2d43111eceeecf1e0da
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
<<<<<<< HEAD
    """/: displays Hello HBNB! """
    return 'Hello HBNB!'
=======
    """ Returns Hello HBNB """
    return "Hello HBNB!"
>>>>>>> dd948381d6da4095df99c2d43111eceeecf1e0da


@app.route('/hbnb', strict_slashes=False)
def hbnb():
<<<<<<< HEAD
    """prints HBNB when /hbnb is called"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """/c/<text>: display C followed by the value of the text variable"""
    return "C " + text.replace('_', ' ')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

=======
    """ Return HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ takes the text and process it """
    return f"C {text.replace('_', ' ')}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
>>>>>>> dd948381d6da4095df99c2d43111eceeecf1e0da
