# [Requests](https://docs.python-requests.org/en/latest/) and [Request](https://docs.python.org/3/library/urllib.request.html)

The `requests` library is a popular Python library for making HTTP requests. It provides a simple and elegant way to interact with web services and APIs. The `requests` library is not part of the Python standard library, so you need to install it separately using `pip`. Meanwhile, the `urllib.request` module is part of the Python standard library and provides similar functionality for making HTTP requests, but it is more low-level and less user-friendly than the `requests` library.

---

## GET

To make a `GET` request using the `requests` library, we can use the `requests.get()` function. This function sends a `GET` request to the specified URL and returns a `Response` object.

### Example
```python
import requests

response = requests.get('https://api.github.com')

print(response.status_code)
print(response.json())
```

To make a `GET` request using the `urllib.request` module, we can use the `urllib.request.urlopen()` function. This function sends a `GET` request to the specified URL and returns a file-like object.

### Example
```python
import urllib.request

response = urllib.request.urlopen('https://api.github.com')

print(response.status)
print(response.read())
```

---

## POST

To make a `POST` request using the `requests` library, we can use the `requests.post()` function. This function sends a `POST` request to the specified URL with the specified data and returns a `Response` object.

### Example
```python
import requests

data = {'key': 'value'}
response = requests.post('https://httpbin.org/post', data=data)

print(response.status_code)
print(response.json())
```

To make a `POST` request using the `urllib.request` module, we can use the `urllib.request.urlopen()` function with the `data` parameter. This function sends a `POST` request to the specified URL with the specified data and returns a file-like object.

### Example
```python
import urllib.parse
import urllib.request

data = urllib.parse.urlencode({'key': 'value'}).encode('utf-8')
request = urllib.request.Request('https://httpbin.org/post', data=data, method='POST')
response = urllib.request.urlopen(request)

print(response.status)
print(response.read())
```

---

## Headers

To send custom headers with a request using the `requests` library, we can pass a `headers` dictionary to the `requests.get()` or `requests.post()` function.

### Example
```python
import requests

headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get('https://api.github.com', headers=headers)

print(response.status_code)
print(response.json())
```

To send custom headers with a request using the `urllib.request` module, we can create a `Request` object and set the `headers` attribute.

### Example
```python
import urllib.request

request = urllib.request.Request('https://api.github.com', headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(request)

print(response.status)
print(response.read())
```

---

## Authentication

To send authentication credentials with a request using the `requests` library, we can pass a `auth` tuple to the `requests.get()` or `requests.post()` function.

### Example
```python
import requests

auth = ('username', 'password')
response = requests.get('https://api.github.com', auth=auth)

print(response.status_code)
print(response.json())
```

To send authentication credentials with a request using the `urllib.request` module, we can create a `Request` object and set the `auth` attribute.

### Example
```python
import urllib.request

auth_handler = urllib.request.HTTPBasicAuthHandler()
auth_handler.add_password(
    passwd='password',
    realm='realm',
    uri='https://api.github.com',
    user='username',
)
opener = urllib.request.build_opener(auth_handler)
response = opener.open('https://api.github.com')

print(response.status)
print(response.read())
```
