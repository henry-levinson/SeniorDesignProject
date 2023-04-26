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
 Provide an overview of the code structure.
 List the main files and directories and explain their purposes.
 Use code snippets or diagrams if necessary.
### Root Directory
 Describe the root directory and its contents.
### Static Directory
 Describe the static directory and its contents.
 Provide details of any files within the directory.
### Templates Directory
 Describe the templates directory and its contents.
 Provide details of any files within the directory.
### app.py
 Describe the app.py file and its contents.
 Explain the purpose of the file and how it fits into the application.
### db_init.py
 Describe the db_init.py file and its contents.
 Explain the purpose of the file and how it fits into the application.

## Contributors
 List the names of contributors who worked on the project.
 Provide contact details if available.