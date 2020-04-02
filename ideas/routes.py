
import random  
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


def getIdea(category):
    ideas = db.session.query(category).all()
    x = random.randint(0,len(ideas)-1)
    idea = ideas[x]
    return idea


@app.route('/')
@app.route('/index')
@app.route('/home', methods=['GET', 'POST'])
def home(): 
    if request.method == "POST":
        category = request.form.get('category') 

        if category == 'kids':
            tag = 'Something to do with Kids'
        elif category == 'listen':
            tag = 'Something to Listen to'
        elif category == 'grateful':
            tag = "Something to be grateful for"
        elif category == 'health':
            tag = 'For your Mental Health'
        else:
            tag = 'Something to ' + category

        category = eval(category)
        idea = getIdea(category)
        return render_template("index.html", idea=idea, category=category, tag=tag)

    return render_template("index.html")


 
