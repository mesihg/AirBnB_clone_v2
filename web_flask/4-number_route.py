#!/usr/bin/python3
"""Flask web application
Must be listening on 0.0.0.0, port 5000
Routes:
     /: display "Hello HBNB!"
     /hbnb: display "HBNB"
     /c/<text>: display "C" followed by the value of the text
     /python/(<text>): display "Python", followed by the value of the text
     /number/<n>: display "n is a number" only if n is an integer
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """Displays HBNB"""
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_route(text):
    """Display "C" followed by the value of the text variable"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_route(text="is cool"):
    """Display "Python" followed by the value of the text variable"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<n>', strict_slashes=False)
def number_route(n):
    """Display "n is a number" only if n is an integer"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
