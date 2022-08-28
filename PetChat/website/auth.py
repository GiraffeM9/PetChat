# Backend to handle authentication - log in system

from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .functions import *
from .email_sender import send_email

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()
        # checks database to see if user exists
        if user:
            if check_password_hash(user.password, password):
                #flash('Logged in!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Password is incorrect.', category='error')
        else:
            flash('Username does not exist', category='error')

    return render_template("login.html")

@auth.route("/sign_up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get("email")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        # check if email/username already exists 
        email_exists = User.query.filter_by(email=email).first()
        username_exists = User.query.filter_by(username=username).first()
        if email_exists:
            flash('Email is already in use.', category='error')
        elif username_exists:
            flash('Username already exists.', category='error')
        # double check password input
        elif password1 != password2:
            flash('Password does not match.', category='error')
        # validation of username/password/email
        elif len(username) < 2:
            flash('Username is too short.', category='error')
        elif len(password1) < 6:
            flash('Password is too short.', category='error')
        elif len(email) < 4:
            flash("Email is invalid.", category='error')
        else:
            # if login details are valid to create an account
            new_user = User(id = generate_id(), email=email, username=username, password=generate_password_hash(password1, method='sha256'))
            send_email("Welcome to PetChat! *", [new_user], "Welcome to PetChat! Here is a 50c sign up bonus, play minigames and participate in events to earn more coins!")
            send_email("Launch Event, ")
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
        
            #flash('User created!')
            return redirect(url_for('views.home'))

    return render_template("signup.html")

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))