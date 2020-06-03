from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/")
def home_page():
    return render_template("index.html", title="chicagodiner", artist="kota")


@app.route("/return_page")
def return_page():
    return render_template("return.html", title="chicagodiner", artist="kota")


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
