from flask import Flask
from flask import render_template

import redis

app = Flask(__name__)
DEBUG=True

@app.route('/signup')
def signup():
    error = None
    return render_template('signup.html', error=error)

@app.route('/')
def login():
    error = None
    return render_template('login.html', error=error)

@app.route('/home')
def home():
    return render_template('home.html', timeline=[{"username": "dummy_username",
                                                    "ts": "today",
                                                    "text": "dummy text"}])

if __name__ == "__main__":
    app.run()
