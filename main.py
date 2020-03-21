from flask import Flask
from flask import render_template

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Phil'}
    return render_template("index.html", title='Quarantine Ideas', user=user)

