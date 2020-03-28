import os
import random
from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask import render_template, url_for,  redirect, request
from ideas import app, db

# map to db
cook = db.Table('cook', db.metadata, autoload=True, autoload_with=db.engine)
do = db.Table('do', db.metadata, autoload=True, autoload_with=db.engine)
donate = db.Table('donate', db.metadata, autoload=True, autoload_with=db.engine)
kids = db.Table('kids', db.metadata, autoload=True, autoload_with=db.engine)
listen = db.Table('listen', db.metadata, autoload=True, autoload_with=db.engine)
watch = db.Table('watch', db.metadata, autoload=True, autoload_with=db.engine)
read = db.Table('read', db.metadata, autoload=True, autoload_with=db.engine)
grateful = db.Table('grateful', db.metadata, autoload=True, autoload_with=db.engine)
health = db.Table('health', db.metadata, autoload=True, autoload_with=db.engine)

# form for buttons
class ideaForm(FlaskForm):
    cookField = SubmitField('Something to cook')
    doField = SubmitField('Something to do')
    donateField = SubmitField('Somewhere to donate')
    kidsField = SubmitField('Something to do with kids')
    listenField = SubmitField('Something to listen to')
    watchField = SubmitField('Something to watch')
    readField = SubmitField('Something to read')
    gratefulField = SubmitField('Something to be grateful for')
    healthField = SubmitField('Something for your mental health')


@app.route('/')
@app.route('/index')
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = ideaForm()

    if request.method == "POST":
        if form.cookField.data:
            cook_ideas = db.session.query(cook).all()
            x = random.randint(0, len(cook_ideas)-1)
            idea = cook_ideas[x]
            return render_template("index.html", title='Pandemic Tool Kit', idea=idea, form=form)

        if form.doField.data:
            do_ideas = db.session.query(do).all()
            x = random.randint(0, len(do_ideas)-1)
            idea = do_ideas[x]
            return render_template("index.html", title='Pandemic Tool Kit', idea=idea, form=form)

        if form.kidsField.data:
            kids_ideas = db.session.query(kids).all()
            x = random.randint(0, len(kids_ideas)-1)
            idea = kids_ideas[x]
            return render_template("index.html", title='Pandemic Tool Kit', idea=idea, form=form)

        if form.watchField.data:
            watch_ideas = db.session.query(watch).all()
            x = random.randint(0, len(watch_ideas)-1)
            idea = watch_ideas[x]
            return render_template("index.html", title='Pandemic Tool Kit', idea=idea, form=form)

        if form.readField.data:
            read_ideas = db.session.query(read).all()
            x = random.randint(0, len(read_ideas)-1)
            idea = read_ideas[x]
            return render_template("index.html", title='Pandemic Tool Kit', idea=idea, form=form)

        if form.listenField.data:
            listen_ideas = db.session.query(listen).all()
            x = random.randint(0, len(listen_ideas)-1)
            idea = listen_ideas[x]
            return render_template("index.html", title='Pandemic Tool Kit', idea=idea, form=form)
    
        if form.gratefulField.data:
            grateful_ideas = db.session.query(grateful).all()
            x = random.randint(0, len(grateful_ideas)-1)
            idea = grateful_ideas[x]
            return render_template("index.html", title='Pandemic Tool Kit', idea=idea, form=form)

        if form.donateField.data:
            donate_ideas = db.session.query(donate).all()
            x = random.randint(0, len(donate_ideas)-1)
            idea = donate_ideas[x]
            return render_template("index.html", title='Pandemic Tool Kit', idea=idea, form=form)

        if form.healthField.data:
            health_ideas = db.session.query(health).all()
            x = random.randint(0, len(health_ideas)-1)
            idea = health_ideas[x]
            return render_template("index.html", title='Pandemic Tool Kit', idea=idea, form=form)
    
    return render_template("index.html", title='Pandemic Tool Kit', form=form)


 