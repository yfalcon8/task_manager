### Enjoy This App Online:
### [Task Manager](http://todotada.herokuapp.com "ToDo to TaDa")


## Table of Contents

* [About](#about)
* [Technologies](#tech)
* [Run Locally](#run)

## <a name="about"></a>About

Five ladies came together to share their love of learning to code.

Users, get ready to visualize the progress of your tasks and goals. 

## <a name="tech"></a>Technologies

[Python 2.7](https://www.python.org/ "Python")    | [Javascript](https://www.python.org/ "Javascript")
:----------- | -----------:
**[Flask](http://flask.pocoo.org/ "Flask")**           | **[jQuery](https://jquery.com/ "jQuery")**           | 
**[SQLAlchemy](http://www.sqlalchemy.org/ "SQLAlchemy")**           | **[Jinja2](http://jinja.pocoo.org/ "Jinja2")** & **[Bootstrap](http://getbootstrap.com/ "Bootstrap")**           | 
**[AJAX / JSON](https://api.jquery.com/category/ajax/ "AJAX")**           |  **[Google Calendar API](https://dev.twitter.com/ "Google Calendar")**

**Dependencies:** [requirements.txt](requirements.txt "Dependencies")

**Test Coverage:** [xx% unittest coverage](tests.py)

## <a name="run"></a>Run Locally
### Flask App

Create a local directory to work within

	$ mkdir -p YOUR_DIRECTORY_NAME_HERE

Clone this repository and cd into it
	
	$ git clone https://github.com/<username>/task-manager YOUR_DIRECTORY_NAME_HERE
	
	$ cd ~/YOUR_DIRECTORY_NAME_HERE

Create your python [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/ "VirtualEnv") and activate it

	$ virtualenv env
	
	$ source env/bin/activate

Install the required Python packages & dependencies
	
	$ pip install -r requirements.txt

Visit the [API](#api) locations and get a secret_key for each.

Create a secrets.sh file

	$ touch secrets.sh YOUR_DIRECTORY_NAME_HERE

Open and add (or simply CAT on the command line) your secret keys into secrets.sh
 
	export GOOGLE_API_KEY = "REPLACE_WITH_YOUR_KEY"  
	export TWILLIO_API_KEY = "REPLACE_WITH_YOUR_KEY" 

Give your app access to this file

	$ source secrets.sh

In your command line, start up the Flask server
	
	$ python server.py
	
In your browser, visit localhost:5000

Enjoy!
