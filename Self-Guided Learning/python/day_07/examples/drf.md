# [Django Rest Framework](https://www.django-rest-framework.org/)

Django Rest Framework is a powerful and flexible toolkit for building Web APIs.

---

# [Configuration](https://www.django-rest-framework.org/#installation)

As a third-party package, Django Rest Framework needs to be listed in the `INSTALLED_APPS` setting of your Django project.

### Example
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

Also for login and logout views, you need to add the following to your `urls.py`:

### Example
```python
from django.urls import path, include

urlpatterns = [
    ...
    path('api-auth/', include('rest_framework.urls')),
]
```

---

## [Models](https://www.django-rest-framework.org/api-guide/serializers/#modelserializer)

Django Rest Framework works well with Django models. As in Django, models are the data structure of your application.

### Example
```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    birth_date = models.DateField()
```

Those models can be serialized using the `ModelSerializer` class.

---

## [Serializers](https://www.django-rest-framework.org/api-guide/serializers/)

Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML, or other content types.

### Example
```python
from rest_framework import serializers
from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'email', 'birth_date']
```

You may also specify new fields that are not present in the model using the `SerializerMethodField`.

### Example
```python
from rest_framework import serializers
from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
    number_of_characters = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ['name', 'email', 'birth_date', 'number_of_characters']

    def get_number_of_characters(self, obj):
        return len(obj.name)
```

`SerializerMethodField` is a read-only field that gets its value by calling a method on the serializer class it is attached to - it will look up for a method named `get_<field_name>`. Pythonic magic!

---

## [Views](https://www.django-rest-framework.org/api-guide/viewsets/)

Django Rest Framework provides a powerful and flexible toolkit for building Web APIs. Usually we use `APIView` or `ViewSet` classes to define the views.

### Example
```python
from rest_framework import viewsets
from .models import Author
from .serializers import AuthorSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
```

The `ModelViewSet` class provides the implementation for CRUD operations by default: `list`, `create`, `retrieve`, `update`, and `destroy`. You can also override the methods to customize the behavior.

### Example
```python
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Author
from .serializers import AuthorSerializer

class AuthorViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Author.objects.all()
        serializer = AuthorSerializer(queryset, many=True)

        return Response(serializer.data)
```

With the `APIView` class, you can define the methods you want to implement.

### Example
```python
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Author
from .serializers import AuthorSerializer

class AuthorList(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)

        return Response(serializer.data)
```

---

## [Authentication](https://www.django-rest-framework.org/api-guide/authentication/) and [Permissions](https://www.django-rest-framework.org/api-guide/permissions/)

Django Rest Framework provides a flexible system for handling authentication and permissions.

### Example
```python
from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff
```

You can use the `permission_classes` attribute to specify the permissions that a view should have.

### Example
```python
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Author
from .serializers import AuthorSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
```

With the `APIView` class, you can specify the permissions in the same way.

### Example
```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Author
from .serializers import AuthorSerializer

class AuthorList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)

        return Response(serializer.data)
```

You can also create custom permissions and authentication classes.

### Example
```python
from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff
```

### Example
```python
from rest_framework.authentication import BaseAuthentication

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        ...
```

And then you just need to use them in your views.

### Example
```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Author

class AuthorList(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [CustomAuthentication]

    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)

        return Response(serializer.data)

```
