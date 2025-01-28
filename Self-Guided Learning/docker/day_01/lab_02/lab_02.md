# Lab 02: Building

With Docker installed, we can now start building our first Docker image. In this lab, we'll create a simple Dockerfile that will build an image for a simple web server.

## Prerequisites

- Docker installed on your system
- A text editor of your choice

## Instructions

1. Create a new directory for this lab and navigate to it.
2. Create a new file named `Dockerfile` in the directory.
3. Open the `Dockerfile` in your text editor.
4. Add the following content to the `Dockerfile`:

```Dockerfile
FROM nginx:alpine

COPY index.html /usr/share/nginx/html/index.html
```

This Dockerfile uses the `nginx:alpine` image as the base image and copies an `index.html` file to the default web root directory.

5. Create a new file named `index.html` in the same directory.
6. Open the `index.html` file in your text editor.
7. Add the following content to the `index.html` file:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Hello, Docker!</title>
</head>
<body>
    <h1>Hello, Docker!</h1>
</body>
</html>
```

This `index.html` file contains a simple HTML document with a heading that says "Hello, Docker!".

8. Build the Docker image using the following command:

```bash
docker build -t simple-web-server .
```

This command builds a Docker image with the tag `simple-web-server` using the `Dockerfile` in the current directory.
