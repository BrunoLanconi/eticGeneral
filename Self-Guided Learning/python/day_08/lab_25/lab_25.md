# Lab 25: Model, View and Template

In this lab, you will adapt the Django project created in the previous lab to include a model, view, and template.

## Prerequisites

- Python 3.x installed on your system
- A text editor of your choice

## Instructions

1. In the `django_project`, create a new app called `blog`.

```bash
$ python manage.py startapp blog
```

2. Create a model in the `blog` app called `Post` with the following fields:

- `title` (CharField)
- `content` (TextField)
- `created_at` (DateTimeField)
- `updated_at` (DateTimeField)
- `published` (BooleanField)

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
```

3. Create a view in the `blog` app called `post_list` that retrieves all the posts from the database and renders them using a template called `post_list.html`.

```python
from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
```

4. Create a template called `post_list.html` in the `blog/templates/blog` directory that displays the list of posts.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Post List</title>
</head>
<body>
    <h1>Post List</h1>
    <ul>
        {% for post in posts %}
            <li>{{ post.title }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

5. Add the `blog` app to the `INSTALLED_APPS` list in the `django_project/settings.py` file.

```python
INSTALLED_APPS = [
    ...
    'blog',
]
```

6. Update the `urls.py` file in the `blog` app to include a URL pattern for the `post_list` view. If the `urls.py` file does not exist, create it.

```python
from django.urls import path
from .views import post_list

urlpatterns = [
    path('', post_list, name='post_list'),
]
```

7. Update the `urls.py` file in the `django_project` directory to include the URL pattern for the `blog` app.

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
```

8. Make and apply the migrations for the `blog` app.

```bash
$ python manage.py makemigrations blog
$ python manage.py migrate
```

9. Run the Django development server and navigate to `http://localhost:8000/` to see the list of posts.

```bash
$ python manage.py runserver
```

You should see an empty list of posts on the page. We will add the ability to create new posts in the next lab.
