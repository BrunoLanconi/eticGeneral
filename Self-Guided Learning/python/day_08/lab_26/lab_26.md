# Lab 26: Website and Admin

In this lab, you will adapt the Django project from the previous lab to a post page and access the admin interface.

## Prerequisites

- Python 3.x installed on your system
- A text editor of your choice

## Instructions

1. In the `django_project`, on `blog` add the `Post` model to the admin interface.

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

2. Create a superuser to access the admin interface.

```bash
$ python manage.py createsuperuser
```

3. Start the development server and access the admin interface at `http://localhost:8000/admin/`.

```bash
$ python manage.py runserver
```

4. Log in with the superuser credentials created in step 2 and add a few posts.
5. Add some posts to the database using the admin interface.
6. Create a view in the `blog` app called `new_post` that allows users to create a new post.

```python
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/new_post.html', {'form': form})
```

7. Create the form in the `blog/forms.py` file.

```python
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'published']
```

7. Create a template called `new_post.html` in the `blog/templates/blog` directory that displays a form to create a new post.

```html
<!DOCTYPE html>
<html>
<head>
    <title>New Post</title>
</head>

<body>
    <h1>New Post</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

8. Add a URL pattern for the `new_post` view in the `blog/urls.py` file.

```python
from django.urls import path
from .views import post_list, new_post

urlpatterns = [
    path('', post_list, name='post_list'),
    path('new_post/', new_post, name='new_post'),
]
```

9. Update the `post_list.html` template to include a link to the `new_post` view.

```html
...
<body>
    ...
    <a href="{% url 'new_post' %}">New Post</a>
</body>
...
```

10. Test the new post creation functionality by accessing the `http://localhost:8000/new_post/` URL in your browser.
11. Now let's create a dedicated page for each post. Create a view in the `blog` app called `post_detail` that displays the details of a post.

```python
from django.shortcuts import render
from .models import Post

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
```

12. Create a template called `post_detail.html` in the `blog/templates/blog` directory that displays the details of a post.

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ post.title }}</title>
</head>

<body>
    <h1>{{ post.title }}</h1>
    <p>{{ post.content }}</p>
</body>
</html>
```

13. Add a URL pattern for the `post_detail` view in the `blog/urls.py` file.

```python
from django.urls import path
from .views import post_list, new_post, post_detail

urlpatterns = [
    path('', post_list, name='post_list'),
    path('new_post/', new_post, name='new_post'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
]
```

14. Update the `post_list.html` template to include a link to the `post_detail` view for each post.

```html
...
<body>
    ...
    <ul>
        {% for post in posts %}
            <li>
                <a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a>
            </li>
        {% endfor %}
    </ul>
</body>
...
```

15. Test the post detail functionality by clicking on a post title in the post list view.
16. Update the `post_detail` view to handle the case where a post with the specified primary key does not exist.

```python
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
```

17. Test the post detail functionality by accessing a non-existent post URL (e.g., `http://localhost:8000/post/999/`).
18. To finish, let's style the website. Create a CSS file called `styles.css` in the `blog/static/blog` directory.

```css
body {
    font-family: Arial, sans-serif;
}

h1 {
    color: #333;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    margin-bottom: 10px;
}

a {
    text-decoration: none;
    color: #007bff;
}

a:hover {
    text-decoration: underline;
}
```

19. Create a `base.html` template in the `blog/templates/blog` directory that includes the CSS file.

```html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Blog{% endblock %}</title>
    <link rel="stylesheet" type="text/css" href="{% static 'blog/styles.css' %}">
</head>

<body>
    {% block content %}
    {% endblock %}
</body>
</html>
```

20. Update `new_post.html`, `post_list.html`, and `post_detail.html` templates to extend the `base.html` template.

```html
# new_post.html

{% extends 'blog/base.html' %}

{% block title %}New Post{% endblock %}

{% block content %}
<h1>New Post</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>

{% endblock %}
```

```html
# post_list.html

{% extends 'blog/base.html' %}

{% block title %}Post List{% endblock %}

{% block content %}
<h1>Post List</h1>
<ul>
    {% for post in posts %}
    <li>
        <a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a>
    </li>
    {% endfor %}
</ul>
<a href="{% url 'new_post' %}">New Post</a>
{% endblock %}
```

```html
# post_detail.html

{% extends 'blog/base.html' %}

{% block title %}{{ post.title }}{% endblock %}

{% block content %}
<h1>{{ post.title }}</h1>
<p>{{ post.content }}</p>
{% endblock %}
```

21. Add ´STATIC_ROOT´ to the `settings.py` file.

```python
...
STATIC_ROOT = BASE_DIR / "static"
...
```

22. Run the `collectstatic` command to collect the static files into the `STATIC_ROOT` directory.

```bash
$ python manage.py collectstatic
```

23. Test the website by running the development server and navigating to `http://localhost:8000/`.

```bash
$ python manage.py runserver
```
