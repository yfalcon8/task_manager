"""Server file for Task Manager."""

#Import necessary modules, etc.
#Access local env variables
import jinja2
import os
import sys

#Utilize Jinja for HTML templates
from jinja2 import StrictUndefined
#Utilize Flask libraries
from flask import Flask, render_template, request, flash, redirect, session, url_for, jsonify

#Use toolbar for debugging
# from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, Places

#Instantiates Flask and "__name__" informs Flask where to find files
app = Flask(__name__, static_url_path='/static')
#Set a secret key to enable the flask session cookies and the debug toolbar
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY", "seKriTz")
#Raises an error when an undefined variable is used in Jinja2
app.jinja_env.undefined = StrictUndefined
#Prevents the need to restart server when HTML/CSS is changed
app.jinja_env.auto_reload = True


###################### Core Routes ##########################

@app.route('/')
def index():
    """Homepage."""

    # if session['_flashes'][0][1] == 'Login successful!':
    #     return redirect('/registration-success')

    return render_template("static/all_goals.html")


################ Login/out Registration #####################


@app.route("/go_register")
def register_page():
    """Send to registration form"""

    return render_template("register.html")


@app.route("/register", methods=['POST'])
def register_form():
    """Register user"""

    #Accept data from input fields
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    phone_number = request.form.get('phone_number')

    #Commit new user details to the database
    user = User(email=email,
                username=username,
                password=password,
                phone_number=phone_number,
                )
    db.session.add(user)
    db.session.commit()

    #Send confirmation msg and back to home page
    flash("Welcome, new user. Wanna get things done?")
    return redirect("/")


@app.route('/login', methods=['POST'])
def login_form():
    """Process login form"""

    #Accept data from input fields
    username = request.form.get("username")
    password = request.form.get("password")

    #Do these credentials align within the database?
    uq = User.query
    user_object = uq.filter_by(email=username).first()
    if user_object.email == username and user_object.password == password:
        flash("Hi again!")
        session["user_email"] = user_object.email
        session["user_id"] = user_object.user_id
        user_id = user_object.user_id
    else:
        flash("Oops! Email / Password mismatch: Try again.")
        
    return redirect("/")


@app.route('/logout', methods=['POST'])
def logout_form():
    """Process logout form"""

    #Remove session and notify user
    session.clear()
    flash("Logged out. Don't be gone for too long!")
    return redirect("/")


################### Helper Functions #######################


# Listening or requests
if __name__ == "__main__":

    connect_to_db(app)
    #Create tables from models.py
    db.create_all(app=app)
    #Set debug=True in order to invoke the DebugToolbarExtension
    # app.debug = True

    # app.config['TRAP_HTTP_EXCEPTIONS'] = True
    # app.config['Testing'] = True
    #Use of debug toolbar
    # DebugToolbarExtension(app)

    #Run app locally (simple)
    app.run(host='0.0.0.0')

    #Run app locally (full)
    #Points to port to use and turns on debugger
    app.run(port=5000, debug=True, host='0.0.0.0')

    #Run app via Heroku
    # PORT = int(os.environ.get("PORT", 5000))
    # app.run(host="0.0.0.0", port=PORT)

