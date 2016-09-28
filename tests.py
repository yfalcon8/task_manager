import unittest
from unittest import TestCase
from server import app
from model import connect_to_db, db, User


class FlaskRouteTests(TestCase):
    """Flask tests."""

############### Testing Necessities ##############

    def setUp(self):
        """Stuff to do before every test."""

        #Get the Flask test client
        self.client = app.test_client()

        #Show Flask errors that happen during tests
        app.config['TESTING'] = True


################### Test Routes ##################

    def test_home_route(self):
        """Test route to homepage."""

        result = self.client.get("/")
        self.assertEqual(result.status_code, 200)
        # self.assertIn('Connect!', result.data)

################# Test Database #################

class FlaskTestDatabase(TestCase):
    """Flask tests that use the test database"""

    def setUp(self):
        """Things to do before each test"""

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
        db.session.add_all([self.places_1, self.places_2])
        #Commit changes
        db.session.commit()

    def test_find_place(self):
        """Can we find a place in the database"""

        #Query the database for a user
        place = Places.query.filter_by(name='Transamerica Pyramid Center').first()
        #What the result of query should be:
        self.assertEqual(place.wifi, 'no')

    def tearDown(self):
        """Things to do at end of every test"""

        #Close the session
        db.session.close()
        #Drop the database
        db.drop_all()


if __name__ == "__main__":
    unittest.main()

