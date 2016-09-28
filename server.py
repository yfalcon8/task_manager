from jinja2 import StrictUndefined

# Flask: A class that we import. An instance of this class will be the
# WSGI application.

from flask import Flask, render_template, request, flash, redirect, url_for, jsonify

#######################
#### configuration ####
#######################

# Instantiates Flask. "__name__" is a special Python variable for the name of
# the current module. This is needed so that Flask knows where to look for
# templates, static files, and so on.
app = Flask(__name__)

# Raises an error when an undefined variable is used in Jinja2.
app.jinja_env.undefined = StrictUndefined

# Prevents the need to restart server when HTML/CSS is changed.
app.jinja_env.auto_reload = True


# @app.route('/') is a Python decorator. '/' in the decorator maps directly
# to the URL the user requested which is the homepage. The index function
# is triggered when the URL is visited.
@app.route('/')
def index():
    """Homepage."""

    # if session['_flashes'][0][1] == 'Login successful!':
    #     return redirect('/registration-success')

    return render_template("static/all_goals.html")


# App will only run if we ask it to run.
if __name__ == "__main__":

    # Setting this to be true so that I can invoke the DebugToolbarExtension
    # app.debug = True

    # connect_to_db(app)

    # Create the tables we need from our models (if they already
    # exist, nothing will happen here, so it's fine to do this each
    # time on startup)
    # db.create_all(app=app)

    # debug=True runs Flask in "debug mode". It will reload my code when it
    # changes and provide error messages in the browser.
    # The host makes the server publicly available by adding 0.0.0.0. This
    # tells my operating system to listen on all public IPs.
    # Port 5000 required for Flask.
    app.run(port=5000, debug=True, host='0.0.0.0')
