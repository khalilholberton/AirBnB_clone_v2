#!/usr/bin/python3
'''script start flask application to listen
 on 0.0.0.0 port 5000 with variables'''

from flask import render_template
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


@app.route('/number/<int:n>')
def display_num(n):
    """
    print n  only if int
    """
    return ("{:d} is a number".format(n))


@app.route('/number_template/<int:n>')
def display_template_with_num(n):
    """
    display template with n integer
    """
    return (render_template('5-number.html', n=n))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
