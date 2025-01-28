# Lab 23: API with DRF

In this lab, you will create a simple API using Django Rest Framework. This API will behave similarly to the FastAPI API created in the previous lab.

## Prerequisites

- Python 3.x installed on your system
- A text editor of your choice

## Instructions

1. Create a new folder `api-drf` and navigate to it.
2. Initialize Poetry in the folder.
3. Install Django and Django Rest Framework using Poetry.
4. Create a new Django project `api_project` using the following command:

```bash
poetry run django-admin startproject api_project .
```

5. Create a new Django app `api_app` using the following command:

```bash
poetry run python manage.py startapp api_app
```

6. Add the `rest_framework` app to the `INSTALLED_APPS` setting in the `api_project/settings.py` file:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

7. Add the login and logout views to the `api_project/urls.py` file:

```python
from django.urls import path, include

urlpatterns = [
    ...
    path('api-auth/', include('rest_framework.urls')),
]
```

8. Create a new file `serializers.py` in the `api_app` folder and add the following code:

```python
from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['message']
```

9. Create a new file `models.py` in the `api_app` folder and add the following code:

```python
from django.db import models

class Message(models.Model):
    message = models.CharField(max_length=100)
```

10. Create a new file `views.py` in the `api_app` folder and add the following code:

```python
from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
```

11.  Update the `api_app/urls.py` file to include the `MessageViewSet`. If the file does not exist, create it.

```python
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet

router = DefaultRouter()
router.register(r'messages', MessageViewSet)

urlpatterns = router.urls
```

12. Add `api_app` to `INSTALLED_APPS` in the `api_project/settings.py` file and include the `api_app` URLs in the project URLs:

```python
INSTALLED_APPS = [
    ...
    'api_app',
]

```python
from django.urls import path, include

urlpatterns = [
    ...
    path('', include('api_app.urls')),
]
```

13. Migrate and run the Django development server using the following command:

```bash
poetry run python manage.py makemigrations
poetry run python manage.py migrate
poetry run python manage.py runserver
```

14. Open your browser and navigate to `http://localhost:8000/messages/`. You should see the Django Rest Framework interface for the `Message` model.
15. Click on the `Add Message` button and add a new message.
16. Click on the `POST` button to save the message.
17. You should see the message displayed on the page.
18. Let's implement logging in the Django Rest Framework API. Create a new file `middleware.py` in the `api_app` folder and add the following code:

```python
import logging

logging.basicConfig(level=logging.INFO)


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logging.info(f"Request: {request.method} {request.path}")
        response = self.get_response(request)
        logging.info(f"Response: {response.status_code}")
        return response
```

19. Update the `api_project/settings.py` file to include the middleware:

```python
MIDDLEWARE = [
    ...
    'api_app.middleware.LogMiddleware',
]
```

20. Run the Django development server using the following command:

```bash
poetry run python manage.py runserver
```

21. Open your browser and navigate to `http://localhost:8000/messages/`. You should see the Django Rest Framework interface for the `Message` model.
22. Click on the `Add Message` button and add a new message.
23. Click on the `POST` button to save the message.
24. You should see the message displayed on the page.
25. Let's implement the documentation for the Django Rest Framework API. Create a new file `api_app/urls.py` and add the following code:

```python
from rest_framework.documentation import include_docs_urls
from django.urls import path

urlpatterns += [path("docs/", include_docs_urls(title="Message API"))]
```

26. Install coreapi using Poetry:

```bash
poetry add coreapi
```

27. Add `DEFAULT_SCHEMA_CLASS` to the `api_project/settings.py` file:

```python
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
}
```

28. Run the Django development server using the following command:

```bash
poetry run python manage.py runserver
```

29. Open your browser and navigate to `http://localhost:8000/docs/`. You should see the documentation for the Django Rest Framework API.