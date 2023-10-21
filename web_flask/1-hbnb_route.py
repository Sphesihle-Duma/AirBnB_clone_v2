#!/usr/bin/python3
""" Create a flask with two route """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnbn():
    """ Returns Hello Hbnb """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns HBNB """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
