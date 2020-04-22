#!/usr/bin/python3
"""Flask web application.
Host: 0.0.0.0
port: 5000
Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: Displays 'HBNB'
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>.
    /number/<n>: Displays 'n is a number' only if <n> is an integer.
"""
from flask import Flask, abort

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'

    Arguments:
        None

    Returns:
        (str)
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'Hello HBNB!'

    Arguments:
        None

    Returns:
        (str)
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of <text
    Arguments:
        text (text): params
    Returns:
        (str) Replaces _ with spaces in text
    """
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays 'Python' followed by the value of <text
    Arguments:
        text (text): params
    Returns:
        (str) Replaces _ with spaces in text
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displays 'n is a number' if n is an int.

    Arguments:
        n (int): params

    Returns:
        (str)
    """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
