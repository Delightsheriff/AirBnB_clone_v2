#!/usr/bin/python3
"""A script that starts a Flask web application"""

# Import Flask
from flask import Flask, render_template

# Create an instance of Flask
app = Flask(__name__)


# Define the route for /
@app.route('/', strict_slashes=False)
def hello():
    # Return the message to display
    return 'Hello HBNB!'


# Define the route for /hbnb
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    # Return the message to display
    return 'HBNB'


# Define the route for /c/<text>
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    # Replace underscore with space
    text = text.replace('_', ' ')
    # Return the message to display
    return 'C {}'.format(text)


# Define the route for /python/<text>
@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    # Replace underscore with space
    text = text.replace('_', ' ')
    # Return the message to display
    return 'Python {}'.format(text)


# Define the route for /number/<n>
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    # Return the message to display
    return '{} is a number'.format(n)


# Define the route for /number_template/<n>
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    # Render the HTML template with n
    return render_template('5-number.html', n=n)


# Define the route for /number_odd_or_even/<n>
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    # Check if n is odd or even
    if n % 2 == 0:
        parity = 'even'
    else:
        parity = 'odd'
    # Render the HTML template with n and parity
    return render_template('6-number_odd_or_even.html', n=n, parity=parity)


# Run the app on 0.0.0.0, port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
