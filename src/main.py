from flask import Flask, render_template, url_for, redirect, request, session, flash
from functools import wraps

app = Flask(__name__)

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
    return render_template('main.html')

# login 
@app.route('/login', methods=['GET','POST'])
def login():
    error = None

    if request.method == 'POST':
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

if __name__ == '__main__':
    app.run(debug=True)
