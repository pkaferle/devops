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
    check_user = g.db.hexists('users', username)
    if check_user:
        error = 'User already exists.'
        return render_template('signup.html', error=error)

    # Save user to database
    user_id = str(g.db.incrby('next_user_id', 1000))
    g.db.hmset('user:' + user_id, dict(username=username, password=password))
    g.db.hset('users', username, user_id)
    #session['username'] = username
    #return redirect(url_for('home'))
    return 'Welcome %s' % username


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'GET':
        return render_template('login.html', error=error)
    username = request.form['username']
    password = request.form['password']

    user_id = g.db.hget('users', username)
    if not user_id:
        error = 'No such user. Try again.'
        return render_template('login.html', error=error)
    return 'You succesfuly logged in,  %s' % username

if __name__ == "__main__":
    app.run()
