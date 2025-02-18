#!/usr/bin/python3
"""A script that starts a Flask web application"""

# Import Flask
from flask import Flask

# Create an instance of Flask
app = Flask(__name__)


# Define the route for /
@app.route('/', strict_slashes=False)
def hello():
    """ Return the message to display"""
    return 'Hello HBNB!'


# Run the app on 0.0.0.0, port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
