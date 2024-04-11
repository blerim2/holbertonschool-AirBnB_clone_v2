#!/usr/bin/python3
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb_1():
    return("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def hbnb_2(text):
    return("C {}".format(text.replace("_", " ")))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=None)