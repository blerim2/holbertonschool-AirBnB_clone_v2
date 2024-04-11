#!/usr/bin/python3
"""
Module to initiate a flask app
"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    set route
    """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb_1():
    """
    set route
    """
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def hbnb_2(text):
    """
    set route
    """
    return ("C {}".format(text.replace("_", " ")))


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def hbnb_3(text):
    """
    set route
    """
    return ("Python {}".format(text.replace("_", " ")))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=None)
