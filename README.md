# To-Do List Application

A Django-based to-do list application where users can create, manage, and delete tasks (referred to as **listings**) within various categories. This app allows users to register, log in, and manage their to-do list items with customizable priorities and due dates.

## Features

- **User Authentication**: Users can register, log in, and log out of the system.
- **Task Management**: Create, edit, delete, and filter tasks based on categories, priority, and date ranges.
- **Categories**: Users can create categories to group their tasks.
- **Filtering and Sorting**: Tasks can be filtered by search term, priority, and date range. Tasks are sorted by due date and priority.
- **Task Activation**: Each task has an active/inactive status.

## Technologies Used

- **Django**: Python-based web framework for building the backend.
- **Bootstrap**: Front-end framework for styling.
- **SQLite** (or another database): Database to store user data and tasks.

## Installation

Follow these steps to set up the project on your local machine.

### Prerequisites

- **Python 3.x** (preferably Python 3.6 or later)
- **Django 3.x** (or the version specified in `requirements.txt`)

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/TO_DO_LIST.git
    cd TO_DO_LIST
    ```

2. Set up a virtual environment (recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run database migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser for the admin interface (optional, for testing purposes):

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Open your browser and navigate to `http://127.0.0.1:8000/` to access the application.

## Usage

### User Authentication

- **Register**: Users can sign up by providing a username, email, and password. Passwords must be at least 8 characters long and must contain at least one uppercase letter, one lowercase letter, and one digit.
- **Log In**: Users can log in using their credentials.
- **Log Out**: After logging in, users can log out of their accounts.

### Task Management

- **Create Listing**: After logging in, users can create new tasks. Each task must belong to a category and have a specified priority, role, and start/end date.
- **Edit Listing**: Users can edit existing tasks.
- **Delete Listing**: Tasks can be deleted if no longer needed.
- **Search and Filter**: Tasks can be filtered based on:
  - Search term (searches within the role field).
  - Priority.
  - Date range (start and end dates).
  - Tasks are also sorted by due date and priority.

### Categories

- **Create Category**: Users can create categories to organize tasks.
- **View Categories**: A list of all categories will be displayed for the logged-in user.

### Template Overview

- **`task/index.html`**: The home page for the application.
- **`task/login.html`**: Login page for users.
- **`task/register.html`**: Registration page for new users.
- **`task/display_listing.html`**: Page displaying tasks, with options to filter and search.
- **`task/create_listing.html`**: Page to create a new task.
- **`task/edit_listing.html`**: Page to edit an existing task.
- **`task/delete_listing.html`**: Page to confirm the deletion of a task.
- **`task/categories_list.html`**: Page for managing categories.

## File Structure

```bash
.
├── manage.py
├── TO_DO_LIST
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── task
│   ├── migrations
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── templates
│   │   └── task
│   │       ├── index.html
│   │       ├── login.html
│   │       ├── register.html
│   │       ├── display_listing.html
│   │       ├── create_listing.html
│   │       ├── edit_listing.html
│   │       ├── delete_listing.html
│   │       └── categories_list.html
├── db.sqlite3
├── requirements.txt
└── README.md
