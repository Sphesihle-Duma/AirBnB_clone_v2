#!/usr/bin/python3
<<<<<<< HEAD
"""script that starts a Flask web application"""

from flask import Flask
=======
""" Create a flask with two route """
from flask import Flask


>>>>>>> dd948381d6da4095df99c2d43111eceeecf1e0da
app = Flask(__name__)


@app.route('/', strict_slashes=False)
<<<<<<< HEAD
def hello_hbnb():
    """/: displays Hello HBNB"""
    return 'Hello HBNB!'
=======
def hello_hbnbn():
    """ Returns Hello Hbnb """
    return "Hello HBNB!"
>>>>>>> dd948381d6da4095df99c2d43111eceeecf1e0da


@app.route('/hbnb', strict_slashes=False)
def hbnb():
<<<<<<< HEAD
    """prints HBNB when /hbnb is called """
    return 'HBNB'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

=======
    """ Returns HBNB """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
>>>>>>> dd948381d6da4095df99c2d43111eceeecf1e0da
