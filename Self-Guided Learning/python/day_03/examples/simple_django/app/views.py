from django.shortcuts import render  # type: ignore


def index(request):
    context = {
        "phrase": "Hello, World!",
    }

    return render(request, "index.html", context)
