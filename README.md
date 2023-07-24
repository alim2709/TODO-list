# TODO-list
This app can help you create a tasks to manage your time perfectly

Local deployment instruction
To deploy the Task Manager project locally, please follow the steps below:

Clone the repository to your local machine: git clone https://github.com/alim2709/TODO-list.git

Navigate to the project directory: cd TODO-list

Create a virtual environment: python -m venv env

Activate the virtual environment:

For Windows:  .\env\Scripts\activate
For macOS : source env/bin/activate
For Linux : source env/bin/activate
Install the project dependencies: pip install -r requirements.txt

Environment Variables
The following environment variables should be set in the .env file:

SECRET_KEY: Your  secret key
Note: Before starting the project, make a copy of the .env_sample file and rename it to .env. Replace the sample values with your actual environment variable values.

Apply database migrations: python manage.py migrate

Run the development server: python manage.py runserver

Open your web browser and access the Task Manager application at http://localhost:8000/.

You can use test user made during migration:

Username admin
Password test
