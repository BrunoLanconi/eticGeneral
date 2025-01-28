# Lab 24: Project and App

In this lab, you will create a new Django project and a new Django app, and then run the development server.

## Prerequisites

- Python 3.x installed on your system
- A text editor of your choice

## Instructions

1. Create a new folder `django_project` and navigate to it in your terminal.
2. Remember to initialize Poetry and add Django to your project.
3. After installing Django, start a new Django project by running the following command:

```bash
$ django-admin startproject mysite
```

This will create a new directory called `mysite` with the following structure:

```
.
├── manage.py
└── mysite
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

4. Navigate to the `mysite` directory and start the development server by running the following command:

```bash
$ cd mysite
$ python manage.py runserver
```

5. Open your browser and navigate to `http://localhost:8000/`. You should see the Django welcome page.
6. Create a new Django app by running the following command:

```bash
$ python manage.py startapp myapp
```

This will create a new directory called `myapp` with the following structure:

```
.
├── __init__.py
├── admin.py
├── apps.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py
```
