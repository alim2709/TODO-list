# TODO-list
This app can help you create a tasks to manage your time perfectly

Local deployment instruction
To deploy the Task Manager project locally, please follow the steps below:

Clone the repository to your local machine: git clone https://github.com/neostyle88/todo.git

Navigate to the project directory: cd todo

Create a virtual environment: python -m venv env

Activate the virtual environment:

For Windows:  .\env\Scripts\activate
For macOS and Linux: source env/bin/activate
Install the project dependencies: pip install -r requirements.txt

Apply database migrations: python manage.py migrate

Run the development server: python manage.py runserver

Open your web browser and access the Task Manager application at http://localhost:8000/.

You can use test user made during migration:

Username admin
Password test
Environment Variables
The following environment variables should be set in the .env file:

DJANGO_SECRET_KEY: Your Django secret key
Note: Before starting the project, make a copy of the .env_sample file and rename it to .env. Replace the sample values with your actual environment variable values.