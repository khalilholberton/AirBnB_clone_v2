#!/usr/bin/python3
"""Flask web application.
Host: 0.0.0.0
port: 5000
Routes:
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Render the HBnB filters HTML.

    Arguments:
        None

    Returns:
        Render (Html) template 1--hbnb_filters.html
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
