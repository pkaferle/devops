from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import session
from flask import g
from flask import redirect

import redis

app = Flask(__name__)
DEBUG=True

# I am using a SHA1 hash. Use a more secure algo in your PROD work
#SECRET_KEY = '8cb049a2b6160e1838df7cfe896e3ec32da888d7'
#app.secret_key = SECRET_KEY

# Redis setup
DB_HOST = 'localhost'
DB_PORT = 6379
DB_NO = 1

# Before each request, Redis needs to be initiated
def init_db():
    db = redis.StrictRedis(
        host=DB_HOST,
        port=DB_PORT,
        db=DB_NO)
    return db

@app.before_request
def before_request():
    g.db = init_db()


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'GET':
        return render_template('signup.html', error=error)

    # Get the user data from the web page
    username = request.form['username']
    password = request.form['password']

    # TODO: Check if the user already exists

    # Save user to database
    user_id = str(g.db.incrby('next_user_id', 1000))
    g.db.hmset('user:' + user_id, dict(username=username, password=password))
    g.db.hset('users', username, user_id)
    #session['username'] = username
    #return redirect(url_for('home'))
    return 'welcome %s' % username

@app.route('/')
def login():
    error = None
    return render_template('login.html', error=error)

if __name__ == "__main__":
    app.run()
