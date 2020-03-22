from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '348943509rf4j09w09809cv987v987b'

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


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





if __name__ == '__main__': 
    app.run(debug=True)

