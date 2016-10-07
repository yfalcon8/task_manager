import unittest
from unittest import TestCase
from server import app
from model import connect_to_db, db, User


class FlaskRouteTests(TestCase):
    """Flask tests."""

############### Testing Necessities ##############

    def setUp(self):
        """To do before every test."""

        #Get the Flask test client
        self.client = app.test_client()

        #Show Flask errors that happen during tests
        app.config['TESTING'] = True

################### Test Routes ##################

    def test_home_route(self):
        """Test route to homepage."""

        #Go to homepage
        result = self.client.get("/")
        #Does the page render
        self.assertEqual(result.status_code, 200)
        #Does data make it to the DOM
        # self.assertIn('Connect!', result.data)

    def test_login_form(self):
        """Does the login form show"""

        #Go to login form
        result = self.client.get('/login')
        #Does the page render
        self.assertEqual(result.status_code, 200)
        #Should see title of page
        # self.assertIn('<h2>Login</h2>', result.data)

################# Test Database #################

class FlaskTestDatabase(TestCase):
    """Flask tests that use the test database"""

    def setUp(self):
        """To do before each test"""

        #Get the Flask test client
        self.client = app.test_client()
        #Show Flask errors that happen during tests
        app.config['TESTING'] = True
        #Connect to test database
        connect_to_db(app, "postgresql:///testdb")
        #Create tables and add sample data
        db.create_all()
        #Add example data to test database
        """Create some sample data."""

        #In case this is run more than once, empty out existing data
        User.query.delete()

        user_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
        username = db.Column(db.String(64), unique=True, nullable=False)
        password = db.Column(db.String(200), nullable=False)
        profile_img = db.Column(db.String(200), nullable=True)
        email = db.Column(db.String(50), unique=True, nullable=False)
        time_zone = db.Column(db.String(25), nullable=True)
        phone_number = db.Column(db.Integer, nullable=True)


        #Add test example users
        self.user_1 = User(username='Minnie',
                               password='MouseGal',
                               profile_img='static/img/minnie.jpg',
                               email='minnie@mouse.purr',
                               time_zone='PST',
                               phone_number='510-510-5100')
        self.user_2 = User(username='LadyFlash',
                               password='PowerfulLady',
                               profile_img='static/img/ladyflash.jpg',
                               email='lady@flash.pow',
                               time_zone='PST',
                               phone_number='925-925-9255')

        #Add all to the database
        db.session.add_all([self.user_1, self.user_2])
        #Commit changes
        db.session.commit()

    def test_find_user(self):
        """Can we find a user in the database"""

        #Query the database for a user
        user = User.query.filter_by(name='Minnie').first()
        #What the result of query should be:
        self.assertEqual(user.time_zone, 'PST')

    def tearDown(self):
        """Things to do at end of every test"""

        #Close the session
        db.session.close()
        #Drop the database
        db.drop_all()

    def test_find_user(self):
        """Can we find a user in the database"""

        #Query the database for a user
        user = User.query.filter_by(email='lady@flash.pow').first()
        #Query results should be:
        self.assertEqual(user.username, 'LadyFlash')

    def test_process_login(self):
        """Is the login form processed correctly"""

        #Process login form
        result = self.client.post('/login', data={'email': 'lady@flash.pow',
                                  'password': 'PowerfulLady'}, follow_redirects=True)
        #Expect ok status code from / route
        self.assertEqual(result.status_code, 200)
        #Flash message should appear when user logs in
        self.assertIn('Hi again!', result.data)

    def test_process_login_incorrect_password(self):
        """Is login form processed correctly when user types wrong password"""

        #Process login form with incorrect password
        result = self.client.post('/login',
                                  data={'email': 'minnie@mouse.purr',
                                        'password': 'Mousey'}, follow_redirects=True)
        #Should get ok status code from / route
        self.assertEqual(result.status_code, 200)
        #Flash message should appear when user types wrong password
        self.assertIn('Incorrect password', result.data)

    def test_process_login_user_does_not_exist(self):
        """Is login form processed correctly when user is not in database"""

        #Process login form when user does not exists
        result = self.client.post('/login',
                                  data={'email': 'lady@flash.po',
                                        'password': 'PowerfulLady'}, follow_redirects=True)
        #Should get ok status code from / route
        self.assertEqual(result.status_code, 200)
        #Flash message should appear when user is not in database
        self.assertIn('Please create an account', result.data)

    def test_process_registration(self):
        """Is the registration form processed correctly"""

        #Process registration form when user is new
        result = self.client.post('/register', data={'email': 'Test@tester.test',
                                                     'username': 'pswd',
                                                     'password': 99999,
                                                     'phone_number': '888-888-8888'},
                                  follow_redirects=True)
        #Should get ok status code from / route
        self.assertEqual(result.status_code, 200)
        #Flash message should appear when user is not in database
        self.assertIn('Welcome, new user. Wanna get things done?', result.data)

    def test_process_registration_email_already_in_database(self):
        """Is registration form processed correctly when email is already in database"""

        #Process registration form when user email is already in use
        result = self.client.post('/register', data={'email': 'Test@tester.test',
                                                     'username': 'pswd',
                                                     'password': 99999,
                                                     'phone_number': '888-888-8888'},
                                  follow_redirects=True)
        #Should get ok status code from / route
        self.assertEqual(result.status_code, 200)
        #Flash message should appear when user is not in database
        self.assertIn('That email is already taken',
                      result.data)

################# Test Login/out #################

class FlaskTestsLoggedIn(TestCase):
    """Flask test with user logged in to session"""

    def setUp(self):
        """Things to do before each test"""

        #Get the Flask test client
        self.client = app.test_client()
        #Show Flask errors that happen during tests
        app.config['TESTING'] = True
        #Connect to test database
        connect_to_db(app)
        #Add user to the session
        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 10

    def test_base_homepage(self):
        """Test that user is redirected to homepage if logged in"""

        #Go to the homepage, while logged in
        result = self.client.get('/', follow_redirects=True)
        #Should get ok status code from / route
        self.assertEqual(result.status_code, 200)
        #Should see title of page
        # self.assertIn('<h2>Home</h2>', result.data)

    def test_login_form(self):
        """Test that user if redirected to the homepage if logged in"""

        #Go to login form, while logged in
        result = self.client.get('/login', follow_redirects=True)
        #Should get ok status code from / route
        self.assertEqual(result.status_code, 200)
        #Should see title of page
        # self.assertIn('<h2>Login</h2>', result.data)

    def test_logout(self):
        """Is the user able to logout"""

        #Go to logout route
        result = self.client.get('/logout', follow_redirects=True)
        #Should get ok status code from / route
        self.assertEqual(result.status_code, 200)
        #Flash message should appear when user logs out
        # self.assertIn('Logged out. Don't be gone for too long!', result.data)


if __name__ == "__main__":
    unittest.main()

