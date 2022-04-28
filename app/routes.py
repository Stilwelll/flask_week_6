from flask_sqlalchemy import SQLAlchemy
from app import app
from flask import redirect, render_template, url_for
from app.forms import SignUpForm, PhoneBookForm
from app.models import User, Post, PhoneBookInfo


@app.route('/')
def index():
    title = 'Home'
    user = {'id': 1, 'username': 'bstanton', 'email': 'brians@codingtemple.com'}
    return render_template('index.html', current_user=user, title=title)


@app.route('/signup', methods=["GET", "POST"])
def signup():
    title = 'Sign Up'
    form = SignUpForm()
    # check if a post request and that the form is valid
    if form.validate_on_submit():
        # Get data from the validated form
        email = form.email.data
        username = form.username.data
        password = form.password.data
        # Create a new user instance with form data
        new_user = User(email=email, username=username, password=password)
        return redirect(url_for('index'))

    return render_template('signup.html', title=title, form=form)


@app.route('/login')
def login():
    title = 'Log In'
    return render_template('login.html', title=title)

@app.route('/phonebook', methods=["GET", "POST"])
def phonebook():
    title = 'Phone Book'
    form = PhoneBookForm()
    if form.validate_on_submit():
        first_name = form.firstname.data
        last_name = form.lastname.data
        phone_number = form.phonenumber.data
        address = form.address.data
        new_info = PhoneBookInfo(first_name=first_name, last_name=last_name, phone_number=phone_number, address=address)
        return redirect(url_for('index'))

    return render_template('phonebook.html', title=title, form=form)

