# Django API Project

This is a simple Django-based API for managing tasks. It provides basic CRUD (Create, Read, Update, Delete) functionality for tasks. This README provides instructions for setting up, running, and testing the project.

## Prerequisites

Before running the project, make sure you have the following installed:

- Python 3.13.1
- pip (Python package installer)

## Setup

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone git@github.com:Jjat00/todo-api.git
cd todo-api
````

### 2. Create a Virtual Environment
It's recommended to use a virtual environment to manage your project's dependencies. To create and activate a virtual environment, run:

```bash
python -m venv venv
````

Activate the virtual environment:

  * On macOS/Linux:

```bash
source venv/bin/activate
```

  * On Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

Install the required dependencies listed in requirements.txt:

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Some settings, like the Django secret key and allowed hosts, might need to be stored in environment variables.

Create a .env file in the root of your project and add the following:

```env
DJANGO_SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

Replace your_secret_key with a unique secret key for your project. You can generate a secret key by running:

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

```


### 5. Apply Migrations

Before running the server, apply the migrations to set up the database:

```bash
python manage.py migrate
```

### 6. Create a Superuser (Optional)

If you want to access the Django admin panel, you can create a superuser:

```bash
python manage.py createsuperuser
```

You will be prompted to enter a username, email, and password.

### 7. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

### 8. API Endpoints

Here are the available API endpoints:

* GET /api/tasks/: Get a list of all tasks.
* POST /api/tasks/: Create a new task.
* GET /api/tasks/{id}/: Retrieve a specific task by ID.
* PUT /api/tasks/{id}/: Update an existing task by ID.
* DELETE /api/tasks/{id}/: Delete a task by ID.

You can test these endpoints using a tool like Postman or curl.

### 9. Testing the API

To run the tests for the project, use the following command:

```bash
python manage.py test
```

This will run all the test cases and display the results in your terminal.