# Senior Design Project

## Prerequisites
Before you can run this application, you will need to have the following installed:
* [Git](https://git-scm.com/)
* [Python 3.7 or higher](https://www.python.org/downloads/)
* [Flask](https://flask.palletsprojects.com/en/2.1.x/)
* [PostgreSQL](https://www.postgresql.org/)

## Cloning the Repository
To clone the repository and get the source code for this project, follow these steps:

Open a terminal or command prompt and navigate to the directory where you want to store the project files.

Run the following command to clone the repository:

`git clone https://bitbucket.biscrum.com/scm/cwrdg/cwrdg-atp.git`

This will create a new directory called cwrdg-atp in your current directory, containing the project files.

Navigate into the website directory by running the following command:

`cd cwrdg-atp/SeniorDesignProject/flaskwebsite`

## Setup Database and Environment
Open a terminal or command prompt and navigate to the project directory.

Activate the virtual environment by running the following command:

`source venv/bin/activate`

If you are using Windows, the command will be slightly different:

`venv\Scripts\activate`

Install Flask and all other Python packages required by this application by running the following command:

`pip install -r requirements.txt`

Run the following commands to initialize the main database:

`python db_init.py`

`python db_users_init.py`

## Running the Application
Set the Flask app environment variable by running the following command:

`export FLASK_APP=app.py`

If you are using Windows, the command will be slightly different:

`set FLASK_APP=app.py`

Run the application using the following command:

`flask run`

## Code Structure
### Root Directory
(flaskwebsite)

* static directory - contains static assets used in the application, including CSS stylesheets, images, and JavaScript files.
    * css directory - contains CSS stylesheets used in the application.
    * images directory - contains image files used in the application.
    * javascript directory - contains JavaScript files used in the application.
* templates directory - contains the HTML templates used in the application.
    * about.html - the About page template.
    * base.html - the base template which contains the target list.
    * guide.html - the Guide page template.
    * home.html - the Home page template.
    * publications.html - the Publications page template.
    * reviews.html - the Reviews page template.
    * template.html - the header template.
* app.py - the main application file, which contains the Flask application and routing logic.
* databasequerying.py - contains functions for querying the database.
* db_init.py - a script for initializing the main database.
* db_user_init.py - a script for initializing the user database.
* get_protein_info.py - a script for fetching protein information from a remote API.

## Contributors
* Aaditi Mehta
* Anting Ma
* Bryan Nguy
* Henry Levinson
* Malav Patel
* Timothy Schafer