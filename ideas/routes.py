from flask import render_template, url_for, flash, redirect, request
from ideas import app,  db, bcrypt
from ideas.forms import RegistrationForm, LoginForm
from ideas.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

ideas = [
    {
        'suggestion': 'knitting',
        'for': 'creativity, managing anxiety, learning something new, calming', 
        'notes': 'if you have yarn around, its very easy to learn.',
        'by': 'Afi'
    },
    {
        'suggestion': 'go for a walk',
        'for': 'managing anxiety, slowing down',
        'notes': 'feeling the breeze',
        'by': 'Robyn'
    },
    {
        'suggestion': 'jigsaw puzzles',
        'for': 'passing time',
        'notes': "There are some free sites online if you don't have puzzles on hand",
        'by': 'Brisa'
    }
]

@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    user = {'username': 'Phil'}
    return render_template("index.html", title='Quarantine Ideas', user=user, ideas=ideas)


@app.route('/about')
def about():    
    return render_template("about.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data,  password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}. Please log in.', 'success')
        return redirect(url_for('login')) 

    return render_template("register.html",  title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')    
            flash('Login Successful', 'success') 
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else: 
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template("login.html", title='Login', form=form)


@app.route('/logout') 
def logout():
    logout_user()
    return redirect(url_for('home'))
 
@app.route('/account') 
@login_required
def account():
    return render_template('account.html', title='Account')