from flask import render_template, url_for, flash, redirect
from ideas import app
from ideas.forms import RegistrationForm, LoginForm
from ideas.models import User, Post

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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home')) 

    return render_template("register.html",  title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@test.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home')) 
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template("login.html", title='Login', form=form)

