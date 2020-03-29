
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

@app.route('/')
@app.route('/index')
@app.route('/home', methods=['GET', 'POST'])
def home(): 
    if request.method == "POST":
        if request.form.get('cook') == 'cook': 
            cook_ideas = db.session.query(cook).all()
            x = random.randint(0, len(cook_ideas)-1)
            idea = cook_ideas[x]
            return render_template("index.html", idea=idea, category="cook", tag="Something to cook")

        if request.form.get('do') == 'do':
            do_ideas = db.session.query(do).all()
            x = random.randint(0, len(do_ideas)-1)
            idea = do_ideas[x]
            return render_template("index.html", idea=idea, category="do", tag="Something to do")

        if request.form.get('kids') == 'kids':
            kids_ideas = db.session.query(kids).all()
            x = random.randint(0, len(kids_ideas)-1)
            idea = kids_ideas[x]
            return render_template("index.html", idea=idea, category="kids", tag="Something to do with kids")

        if request.form.get('watch') == 'watch':  
            watch_ideas = db.session.query(watch).all()
            x = random.randint(0, len(watch_ideas)-1)
            idea = watch_ideas[x]
            return render_template("index.html", idea=idea, category="watch", tag="Something to watch")

        if request.form.get('read') == 'read':  
            read_ideas = db.session.query(read).all()
            x = random.randint(0, len(read_ideas)-1)
            idea = read_ideas[x]
            return render_template("index.html", idea=idea, category="read", tag="Something to read")

        if request.form.get('listen') == 'listen':  
            listen_ideas = db.session.query(listen).all()
            x = random.randint(0, len(listen_ideas)-1)
            idea = listen_ideas[x]
            return render_template("index.html", idea=idea, category="listen", tag="Something to listen to")

        if request.form.get('grateful') == 'grateful': 
            grateful_ideas = db.session.query(grateful).all()
            x = random.randint(0, len(grateful_ideas)-1)
            idea = grateful_ideas[x]
            return render_template("index.html", idea=idea, category="grateful", tag="Something to be grateful for")

        if request.form.get('health') == 'health':
            health_ideas = db.session.query(health).all()
            x = random.randint(0, len(health_ideas)-1)
            idea = health_ideas[x]
            return render_template("index.html", idea=idea, category="health", tag="For your mental health")

        if request.form.get('donate') == 'donate': 
            donate_ideas = db.session.query(donate).all()
            x = random.randint(0, len(donate_ideas)-1)
            idea = donate_ideas[x]
            return render_template("index.html", idea=idea, category="donate", tag="Something to donate")

    return render_template("index.html")


 
