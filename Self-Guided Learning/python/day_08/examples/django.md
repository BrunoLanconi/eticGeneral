# [Django](https://www.djangoproject.com/)

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

After installing Django, you may start a new Django project by running the following command:

### Example
```bash
$ django-admin startproject mysite
```

This will create a new directory called `mysite` with the following structure:

### Example
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

- `manage.py`: A command-line utility that lets you interact with this Django project.
- `mysite/`: The Python package for the project. Its name is the Python package name you’ll need to use to import anything inside it.
- `mysite/__init__.py`: An empty file that tells Python that this directory should be considered a Python package.
- `mysite/settings.py`: Settings/configuration for this Django project.
- `mysite/urls.py`: The URL declarations for this Django project; a “table of contents” of your Django-powered site.
- `mysite/asgi.py`: An entry-point for ASGI-compatible web servers to serve your project.

Then you can start the development server by running the following command:

### Example
```bash
$ cd mysite
$ python manage.py runserver
```

Or you can create a new Django app by running the following command:

### Example
```bash
$ python manage.py startapp myapp
```

This will create a new directory called `myapp` with the following structure:

### Example
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

- `admin.py`: A configuration file for the Django admin interface.
- `apps.py`: A configuration file for the app.
- `models.py`: A file where you can define the database models for the app.
- `tests.py`: A file where you can define tests for the app.
- `views.py`: A file where you can define the views for the app.
- `migrations/`: A directory where Django stores the migrations for the app.
- `__init__.py`: An empty file that tells Python that this directory should be considered a Python package.

---

## [Models](https://docs.djangoproject.com/en/stable/topics/db/models/)

A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.

### Example
```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```

There is lots of other field types you can use. Below are some of the most common ones:

- `AutoField`: An integer field that automatically increments.

### Example
```python
...
id = models.AutoField(primary_key=True)
...
```

- `BooleanField`: A true/false field.

### Example
```python
...
is_active = models.BooleanField(default=True)
...
```

- `CharField`: A string field.

### Example
```python
...
first_name = models.CharField(max_length=30)
...
```

- `DateField`: A date field.

### Example
```python
...
birth_date = models.DateField()
...
```

- `DateTimeField`: A date and time field.

### Example
```python
...
created_at = models.DateTimeField(auto_now_add=True)
...
```

- `ForeignKey`: A many-to-one relationship.

### Example
```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

- `ManyToManyField`: A many-to-many relationship.

### Example
```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
```

---

## [Views](https://docs.djangoproject.com/en/stable/topics/http/views/)

A view function, or view for short, is a Python function that takes a Web request and returns a Web response. This response can be the HTML contents of a Web page or a redirect, or a 404 error, or an XML document, or an image, etc. The view itself contains whatever arbitrary logic is necessary to return that response.

### Example
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

You may also use View classes instead of functions. Below is an example of a view class:

### Example
```python
from django.http import HttpResponse
from django.views import View

class MyView(View):
    def get(self, request):
        return HttpResponse('Hello, World!')
```

---

## [URLs](https://docs.djangoproject.com/en/stable/topics/http/urls/)

A clean, elegant URL scheme is an important detail in a high-quality Web application. Django encourages beautiful URL design and doesn’t put any cruft in URLs.

### Example
```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

---

## [Templates](https://docs.djangoproject.com/en/stable/topics/templates/)

A template contains the static parts of the desired HTML output as well as some special syntax describing how dynamic content will be inserted. It is a text file using the Django Template Language.

### Example
```html
# templates/polls/detail.html

<!DOCTYPE html>
<html>
<head>
    <title>My Polls</title>
</head>
<body>
    <h1>{{ question.question_text }}</h1>
    <ul>
    {% for choice in question.choice_set.all %}
        <li>{{ choice.choice_text }}</li>
    {% endfor %}
    </ul>
</body>
</html>
```

Then, in your view, you can render the template like this:

### Example
```python
from django.shortcuts import render

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {'question': question})
```

**Note**: You need to edit the `TEMPLATES` setting in your `settings.py` file to tell Django where to look for templates. By default, Django will look for a `templates` directory inside each app - so templates for `myapp` would be in `myapp/templates/myapp`. `<app_name>/templates/<app_name>` may look strange, but it’s a good idea to follow this convention because this is the secure way to avoid conflicts with other apps.

---

## [Settings](https://docs.djangoproject.com/en/stable/topics/settings/)

There are lots of settings you can use to configure Django for your needs. Here are some of the most important ones:

- `BASE_DIR`: The absolute path to the directory where the Django project is located.
- `DATABASES`: A dictionary containing the settings for all databases to be used with Django.
- `DEBUG`: A boolean that turns on/off debug mode. When debug mode is on, you get detailed error pages when things go wrong. When it’s off, you get a simple 404 error page.
- `INSTALLED_APPS`: A list of strings designating all applications that are enabled in this Django installation.
- `MEDIA_ROOT`: The directory where uploaded files will be stored.
- `MEDIA_URL`: URL to use when referring to media files located in `MEDIA_ROOT`.
- `SECRET_KEY`: A secret key for a particular Django installation. This is used to provide cryptographic signing, and should be set to a unique, unpredictable value.
- `STATICFILES_DIRS`: A list of directories where Django will look for additional static files.
- `STATIC_ROOT`: The directory where Django will store static files for deployment.
- `STATIC_URL`: URL to use when referring to static files located in `STATIC_ROOT`.
- `TEMPLATES`: A list of options for specifying the template engine to use, plus some other options.

---

## [Admin](https://docs.djangoproject.com/en/stable/ref/contrib/admin/)

One of the most powerful parts of Django is the automatic admin interface. It reads metadata from your models to provide a quick, model-centric interface where trusted users can manage content on your site. The admin’s recommended use is limited to an organization’s internal management tool. It’s not intended for building your entire front end around.

### Example
```python
from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'published')
    list_filter = ('created_at', 'updated_at', 'published')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'

admin.site.register(Post, PostAdmin)
```

---

## [Authentication](https://docs.djangoproject.com/en/stable/topics/auth/default/)

Django comes with a full-featured and secure authentication system. It handles user accounts, groups, permissions, and cookie-based user sessions.

### Example
```python
from django.contrib.auth import authenticate, login

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
    else:
        # Return an 'invalid login' error message.
```

---

## [Forms](https://docs.djangoproject.com/en/stable/topics/forms/)

Django provides a range of tools and libraries to help you build forms to accept input from site visitors, and then process and respond to the input.

### Example
```python
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
```

Then, in your view, you can use the form like this:

### Example
```python
from django.shortcuts import render

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
```

And in your template, you can render the form like this:

### Example
```html
# templates/name.html

<form method="post">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Submit">
</form>
```

**Note**: The `csrf_token` template tag is used to prevent Cross Site Request Forgeries. It is required for any view that uses Django’s built-in form processing.

---

## [Migrations](https://docs.djangoproject.com/en/stable/topics/migrations/) and [Static Files](https://docs.djangoproject.com/en/stable/howto/static-files/)

Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema. They’re designed to be mostly automatic, but you’ll need to know when to make migrations, when to run them, and the common problems you might run into.

After making changes to your models, you can create a migration by running the following command:

### Example
```bash
$ python manage.py makemigrations
```

Then you can apply the migration by running the following command:

### Example
```bash
$ python manage.py migrate
```

Static files are files that are served directly to the client without any processing from the server. They are typically used for CSS, JavaScript, and images. Django provides a way to manage static files during development and deployment. You can use the `collectstatic` command to collect all static files from your apps into a single location.

### Example
```bash
$ python manage.py collectstatic
```
