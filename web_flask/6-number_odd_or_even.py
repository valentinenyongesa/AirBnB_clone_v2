#!/usr/bin/python3
"""
This is a simple Flask web application with template rendering
"""

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Displays 'C ', followed by the value of the text variable"""
    formatted_text = text.replace('_', ' ')
    return 'C {}'.format(formatted_text)


@app.route('/python/', defaults={'text', 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """Displays 'Python ', followed by the value of the text variable"""
    formatted_text = text.replace('_', ' ')
    return 'Python {}'.format(formatted_text)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    if isinstance(n, int):
        even_or_odd = "even" if n % 2 == 0 else "odd"
        return render_template('6-number_odd_or_even.html', n=n,
                               even_or_odd=even_or_odd)
    else:
        return 'Invalid input. Please provide an integer.'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """Displays a HTML page with H1 tag: 'Number: n'"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
