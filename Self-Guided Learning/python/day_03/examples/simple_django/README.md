# Simple Django

The `Django` module is a Python package for building web applications. It is a powerful tool that can be used to create complex web applications with minimal effort.

## Commands

```bash
bash                           Run a bash shell in the Docker container
build                          Build the Docker image
run                            Run the Django app
help                           Show help
```

---

## [Django](https://www.djangoproject.com/)

Create a new Django project:

```bash
django-admin startproject <project-name> .
```

Create a new Django app:

```bash
python manage.py startapp <app-name>
```

Run the Django app:

```bash
python manage.py runserver
```

---

## Serve [template](https://docs.djangoproject.com/en/5.0/ref/templates/) as main page

1. Create a new directory named `templates` in the app directory.
2. Create a new HTML file in the `templates` directory.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>{{ phrase }}</h1>
</body>
</html>
```

3. Update the `views.py` file to render the template.

```python
from django.shortcuts import render

def index(request):
    context = {
        'phrase': 'Hello, World!'
    }

    return render(request, 'index.html', context)
```

4. Update the `urls.py` file to include the view.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

5. Add the URL configuration to the project's `urls.py` file.

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('app.urls')),
    path('admin/', admin.site.urls),
]
```

6. Make migrations and migrate the database.

```bash
python manage.py makemigrations
python manage.py migrate
```

7. Add `app/templates` to the `DIRS` list in the `TEMPLATES` setting in the project's `settings.py` file.

```python
...

TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR / 'app/templates'],
        ...
    },
]
...
```


8. Run the Django app.

```bash
python manage.py runserver 0.0.0.0:5000
```
