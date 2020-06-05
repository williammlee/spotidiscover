from flask import Flask, render_template, request, redirect, url_for
import main

CLIENT_ID = "480b5435dcf240fdbfb3fa533d5ab00d"
CLIENT_SECRET = "cb1105402e3142b5a52c38f6d44284e8"
app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html")


@ app.route("/loading")
def loading():
    return render_template("loading.html", form_data=request.form['form_data'])


@ app.route("/return_page", methods=['GET', 'POST'])
def return_page():
    if request.method == 'GET':
        render_template("return.html")
        ask_query = request.form['input']
        query = main.main(ask_query)
        main.track(query)
        try:
            main.play(query)
        except:
            redirect("index.html")
    return make_response('POST Request Successful', 200)


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)

# Todo
# if there is an exception with having no audio preview
# if the song is not what they anticipated
# redirect them to a custom page with a nicely formatted album cover, and track info
    # look at the instagram thing as an example.
