from flask import Flask
app = Flask(__name__)

@app.route('/')
def say_hello():
    return '<p>Hello, World, I am a Flask app!</p><p><a href="/about">About</a></p><p><a href="/contact">Contact</a></p>'

@app.route('/about')
def about():
    return '<p>This application is running on the Flask web framework.</p><p><a href="https://flask.palletsprojects.com/">Learn more about Flask</a></p><p><a href="/">Back home</a></p>'

@app.route('/contact')
def contact():
    return '<p>Contact me at: your.email@example.com</p><p><a href="/">Back home</a></p>'
