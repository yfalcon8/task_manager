#######################
#### Configuration ####
#######################

import os

from jinja2 import StrictUndefined
from flask import Flask, render_template, request, flash, redirect, session, jsonify

from form import LoginForm

#Use toolbar for debugging
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, User, Goal, Task
from flask_bcrypt import Bcrypt


# Instantiates Flask and "__name__" informs Flask where to find files.
app = Flask(__name__, static_url_path='/static')

#Set a secret key to enable the flask session cookies and the debug toolbar
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY", "seKriTz")

# Prevents the need to restart server when HTML/CSS is changed.
app.jinja_env.auto_reload = True

# Raises an error when an undefined variable is used in Jinja2.
app.jinja_env.undefined = StrictUndefined

bcrypt = Bcrypt(app)


################ Login/out Registration #####################
@app.route('/')
def home():
    """Homepage that describes the app."""
    return render_template('index.html')
    # form = LoginForm(request.form)

    # return render_template("login.html", form=form)


# @app.route('/login', methods=['GET', 'POST'])
# def login_form():
#     """Process login form."""

#     form = LoginForm(request.form)

#     # Grab the users input.
#     email = request.form.get("email")
#     password = bcrypt.generate_password_hash(request.form.get("password"))

#     # Check that the user exists.
#     uq = User.query
#     user = uq.filter_by(email=email).first()

#     if user and bcrypt.check_password_hash(password, user.password):
#         flash("Hi again!")
#         session["user_email"] = user.email
#         session["user_id"] = user.user_id
#         session["username"] = user.username

#         # return redirect("/landing")
#         return render_template("login.html", form=form)
#     else:
#         flash("Oops! Email / Password mismatch: Try again.")
#         return redirect("/")


# @app.route("/register", methods=['POST'])
# def register_form():
#     """Register user."""

#     # Grab user's inputted data.
#     first = request.form.get('first_name')
#     last_name = request.form.get('last_name')
#     email = request.form.get('email')
#     username = request.form.get('display_name')
#     password = request.form.get('password')
#     password_confirm = request.form.get('password_confirmation')

#     # Make sure 'password' and 'password_confirm' match.
#     if password != password_confirm:
#         flash("The passwords do not match. Please type again.")
#         return redirect("/")

#     # Secure the users pw before storing in database.
#     pw_hash = bcrypt.generate_password_hash(password)

#     # Commit new user to database.
#     user = User(first_name=first,
#                 last_name=last_name,
#                 email=email,
#                 username=username,
#                 password=pw_hash)

#     db.session.add(user)
#     db.session.commit()

#     # Store new user info in session.
#     user_id = db.session.query(User.id).filter_by(email=email).first()[0]
#     session["user_id"] = user_id

#     session["username"] = username
#     session["user_email"] = email

#     # Send confirmation msg and back to home page
#     flash("Welcome, new user. Let's get things done!")
#     return redirect("/landing")


# @app.route('/logout')
# def logout_form():
#     """Process logout form"""

#     # Remove user from session.
#     session.clear()
#     flash("Logged out. Don't be gone for too long!")
#     return render_template("logout.html")


###################### Core Routes ##########################


################ Render information on goals and tasks from Model #############
@app.route('/landing')
def landing():
    """Main page after login/registration."""

#     username = session['username']
#     user_id = session["user_id"]

#     tasks = db.session.query(Task.open_close_status).filter_by(user_id=user_id).all()

#     zero = 0
#     one = 0

#     for task in tasks:
#         if task[0] == 0:
#             zero += 1
#         if task[0] == 1:
#             one += 1

#     # completion_rate = (one / float(zero + one))
#     # print completion_rate

    return render_template("landing.html",
                           username="Minnie")


@app.route('/goals', methods=['GET', 'POST'])
def goals():
    """Displays form for users to add goals. Queries DB to render the user's goals and takes them to goals.html"""

    if request.method == 'POST':
        goal = request.form['goal_name']
        accomplish_by = request.form['goal_date']
        data = {"goal_name": goal, "accomplish_by": accomplish_by}
        return jsonify(data)
        # return render_template('goals.html', goal=goal, accomplish_by=accomplish_by)
    return render_template('goals.html', goal="Enter a goal!", accomplish_by="It takes 21 days to build a habit.")

#     user_id = session['user_id']

#     if Goal.check_by_user_id(user_id) is False:
#         flash("You have no goals currently! Would you like to add one?")
#         return render_template('add_goal.html')
#     else:

#         user = User.check_by_user_id(user_id)
#         goals = Goal.check_by_user_id(user_id)

#     goals = db.session.query(Goal.active_goals).all()
#     description = db.session.query(Goal.description).all()


@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    """Displays form for users to add tasks. Queries DB for user's tasks and takes them to tasks.html"""

    if request.method == 'POST':
        task = request.form['task_name']
        priority = request.form['task_priority']
        freq = request.form['task_frequency']
        accomplish_by = request.form['task_date']
        data = {"task_name": task, "priority": priority, "freq": freq, "accomplish_by": accomplish_by}
        return jsonify(data)
        # return render_template('tasks.html', task_name=task, priority=priority, freq=freq, date=accomplish_by)
    return render_template('tasks.html', task_name=None, priority=None, freq=None, date=None)
#     user_id = session["user_id"]

#     tasks = db.session.query(Task.task_name, Task.due_date).filter_by(user_id=user_id).all()


# # @login_required
# def make_new_task(task_name, due_date, priority, date_added, open_close_status, task_frequency):
#     """Add a new task to the DB"""

#     QUERY = """INSERT INTO Task (task_name, due_date, priority, date_added, open_close_status)
#                VALUES (:task_name, :due_date, :priority, :date_added, :open_close_status)"""

#     db_cursor = db.session.execute(QUERY, {'task_name': task_name,
#                                            'due_date': due_date,
#                                            'priority': priority,
#                                            'date_added': date_added,
#                                            'open_close_status': open_close_status})

#     db.session.commit()

#     print "Successfully added task: {}".format(task_name)


# @app.route('/googlecalendar', methods=['GET'])
# def google_map():
#     return render_template("index-test.html")


# @app.route('/testing')
# def test_page():
#     return render_template("testpage.html")


################### Helper Functions #######################

if __name__ == "__main__":

    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    #Set debug=True in order to invoke the DebugToolbarExtension
    app.debug = True

    # app.config['TRAP_HTTP_EXCEPTIONS'] = True

    DebugToolbarExtension(app)

    connect_to_db(app)
    db.create_all(app=app)

    app.run(port=5000, debug=True, host='0.0.0.0')
