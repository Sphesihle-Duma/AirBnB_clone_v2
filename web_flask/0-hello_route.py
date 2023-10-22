#!/usr/bin/python3
<<<<<<< HEAD
""" Starts a Flash Web Application """

from flask import Flask
=======
""" A script that create simple flask app """
from flask import Flask


>>>>>>> dd948381d6da4095df99c2d43111eceeecf1e0da
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
<<<<<<< HEAD
    """ Prints Hello HBNB! when / is called """
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
=======
    """ returns Hello HBNB """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
>>>>>>> dd948381d6da4095df99c2d43111eceeecf1e0da
