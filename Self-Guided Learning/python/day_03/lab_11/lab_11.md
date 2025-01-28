# Lab 09: Simple Django

In this lab, you will create a simple Django project with a single view that returns a main page with a custom message.

## Prerequisites

- Python 3.x installed on your system
- Poetry installed on your system
- A text editor of your choice

## Instructions

**Attention**: For a better experience, we recommend using a container to isolate the project's dependencies.

1. Create a new directory for this lab and navigate to it.
2. Initialize a new Poetry project:

```bash
poetry init
```

3. Add the `Django` module as a dependency:

```bash
poetry add django
```

4. Create a new Django project:

```bash
poetry run django-admin startproject setup .
```

- `setup` is the name of the project.

5. Create a new Django app:

```bash
poetry run python manage.py startapp app
```

- `app` is the name of the app.

6. Update the `views.py` file to render the main page:

```python
from django.shortcuts import render

def index(request):
    context = {
        'phrase': 'Hello, World!'
    }

    return render(request, 'index.html', context)
```

7. Update the `urls.py` file to include the view:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

8. Add the URL configuration to the project's `urls.py` file:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('app.urls')),
    path('admin/', admin.site.urls),
]
```

9. Make migrations and migrate the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

10. Add `app/templates` to the `DIRS` list in the `TEMPLATES` setting in the project's `settings.py` file:

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

11. Create a new directory called `templates` inside the `app` directory.
12. Create a new file named `index.html` inside the `templates` directory with the following content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Django</title>
</head>
<body>
    <h1>{{ phrase }}</h1>
</body>
</html>
```

13. Run the Django server:

```bash
python manage.py runserver
```

### Optional Challenge

- Edit the `index.html` file to [include a link](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#url) to a new page with a custom message.
- Create a new view and URL configuration to render the new page.
