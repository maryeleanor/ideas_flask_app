
import random  
from flask import render_template, url_for,  redirect, request
from ideas import app, db
 
def map(category):
    table = db.Table(category, db.metadata, autoload=True, autoload_with=db.engine)
    return table

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
        #get category from button press
        category = request.form.get('category')

        #map to db
        table = map(request.form.get('category'))

        # customize tag wording
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

        # run category query to find random idea
        idea = getIdea(table)
        return render_template("index.html", idea=idea, category=category, tag=tag)

    return render_template("index.html")


 
