#!/usr/bin/python3
'''script start flask application to listen
 on 0.0.0.0 port 5000 with variables'''

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """print Hello HBNB"""
    return ("Hello HBNB!")


@app.route('/hbnb')
def display_hbnb():
    """print HBNB"""
    return "HBNB"


@app.route('/c/<var>')
def c(var):
    """print C with variable as given text"""
    return "C " + var.replace('_', ' ')


@app.route('/python')
@app.route('/python/<text>')
def dislay_python(text="is cool"):
    """
    print python with variable as given text and replaces _ with space
    """
    return("Python {}".format(text.replace('_', ' ')))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
