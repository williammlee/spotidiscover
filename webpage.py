from flask import Flask, render_template, request, redirect
from spotify_api import *
from genius_search import *
import webbrowser
import main

CLIENT_ID = "480b5435dcf240fdbfb3fa533d5ab00d"
CLIENT_SECRET = "cb1105402e3142b5a52c38f6d44284e8"
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':
        ask_query = request.form['input']
        main.main(ask_query)
    return render_template("index.html")


@app.route("/return_page", methods=['GET', 'POST'])
def return_page():
    return render_template("return.html", title="chicagodiner", artist="kota")


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
