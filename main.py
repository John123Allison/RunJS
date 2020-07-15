from flask import Flask, render_template, url_for, redirect, request, session, flash, g
from functools import wraps
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# app objects
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.secret_key = "Ku@&'Ug]c#RT6mrr-l!OP2PL%_ho,("


# index page
@app.route('/')
def main():
    return render_template('main.html') # TODO: pass run data thru here
 
@app.route('/login', methods=['GET','POST'])
def login():
    error = None

    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    print("foo")

# connect to database
def connect_db():
    return sqlite3.connect(app.database)

# this runs when the program is started
if __name__ == '__main__':
    app.run(debug=True)
