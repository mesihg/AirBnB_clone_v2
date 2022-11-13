#!/usr/bin/python3
"""Flask web application
Must be listening on 0.0.0.0, port 5000
Routes:
     /: display "Hello HBNB!"
     /hbnb: display "HBNB"
     /c/<text>: display "C" followed by the value of the text
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


if __name__ == "__main__":
    app.run(host="0.0.0.0")
