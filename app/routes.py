from app import app, db
from app.forms import LoginForm, RegistrationForm, RunForm
from app.models import User, Run

from flask import render_template, flash, redirect, request
from flask_login import current_user, login_user, login_required, logout_user, current_user
from werkzeug.urls import url_parse

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
@login_required
def index():
    form = RunForm()
    if form.validate_on_submit():
        run = Run(distance_miles=form.distance_miles.data, time=form.time.data, user_id=current_user.id)
        db.session.add(run)
        db.session.commit()

    curr_user_runs = db.session.query(Run).filter_by(user_id=current_user.id).all()

    return render_template('index.html', title="Home", form=form, runs=curr_user_runs)

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/index')
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect('/login')
        login_user(user, remember=form.remember_me.data)
        # redirect to next page if intercepted with login_required decorator
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = '/index'
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/index')

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/index')

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        flash('Account created')
        return redirect('/login')
    
    return render_template('register.html', title='Register', form=form)