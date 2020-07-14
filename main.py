from flask import Flask, render_template, url_for, redirect, request, session, flash, g
from functools import wraps
import sqlite3

# app objects
app = Flask(__name__)
app.database = "users.db"

app.secret_key = "Ku@&'Ug]c#RT6mrr-l!OP2PL%_ho,("

# add this as a decorator to pages that require a login
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login.')
            return redirect(url_for('login'))
    return wrap

# index page
@app.route('/')
@login_required
def main():
    g.db = connect_db()
    # TODO: get logged in user's run data here using foreign keys
    g.db.close()

    return render_template('main.html') # TODO: pass run data thru here

# login 
@app.route('/login', methods=['GET','POST'])
def login():
    error = None

    if request.method == 'POST':
        # TODO: change this so it queries the db using the g object for a username and pass
        # make sure it's cleaned to be protected from SQL injects
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('Logged in successfully...')
            return redirect(url_for('main'))


    return render_template('login.html', error=error)

# clears login from session and redirects to the main page
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Logged out.')
    return redirect(url_for('main'))

# connect to database
def connect_db():
    return sqlite3.connect(app.database)

# this runs when the program is started
if __name__ == '__main__':
    app.run(debug=True)
