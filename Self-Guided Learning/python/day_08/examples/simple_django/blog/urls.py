from django.urls import path
from .views import new_post, post_detail, post_list

urlpatterns = [
    path("", post_list, name="post_list"),
    path("new_post/", new_post, name="new_post"),
    path("post/<int:pk>/", post_detail, name="post_detail"),
]
