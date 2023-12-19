# Project Tracker

Project Tracker is a Django-based REST API for managing projects, tasks, and user authentication.

## Features

- User authentication (registration and login)
- Project and task management
- RESTful API for accessing and manipulating project and task data
- Token-based authentication for secure API access

## Table of Contents

- [Setup](#setup)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Setup

1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd project_tracker

    Create a Virtual Environment:

    bash

python -m venv venv

Activate the Virtual Environment:

    On Windows:

    bash

.\venv\Scripts\activate

On macOS/Linux:

bash

    source venv/bin/activate

Install Dependencies:

bash

pip install -r requirements.txt

Run Migrations:

bash

python manage.py makemigrations
python manage.py migrate

Create a Superuser (Optional):

bash

python manage.py createsuperuser

Run the Development Server:

bash

    python manage.py runserver

    The API will be accessible at http://127.0.0.1:8000/api/.

API Endpoints

    Projects:
        List and create projects: GET /api/projects/ and POST /api/projects/
    Tasks:
        List and create tasks: GET /api/tasks/ and POST /api/tasks/
    User Registration:
        Register a new user: POST /api/register/
    User Login:
        Log in as a user: POST /api/login/

Usage

    User Registration:
        Create a new user account by making a POST request to /api/register/ with the required user information.

    User Login:
        Log in as a user by making a POST request to /api/login/ with valid credentials. This will return a token for authentication.

    Projects:
        Retrieve the list of projects: GET /api/projects/
        Create a new project: POST /api/projects/

    Tasks:
        Retrieve the list of tasks: GET /api/tasks/
        Create a new task: POST /api/tasks/

Project Structure

    project_tracker/
        Django project settings and configurations.
    tracker/
        Django app containing models, views, serializers, and URLs.

Dependencies

    Django: The web framework for building the project.
    djangorestframework: A powerful toolkit for building Web APIs.
    (Add any other dependencies your project might have)

Contributing

If you'd like to contribute to this project, please follow the Contributing Guidelines.
License

This project is licensed under the MIT License.
