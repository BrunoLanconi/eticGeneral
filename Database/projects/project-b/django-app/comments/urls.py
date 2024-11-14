from comments.views import get_comments
from django.urls import path

urlpatterns = [
    path("<int:phrase_id>/", get_comments, name="comments"),
]
