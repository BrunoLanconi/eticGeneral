from django.urls import path
from sample.views import SamplesView, SampleView

urlpatterns = [
    path("", SamplesView.as_view()),
    path("<str:name>/", SampleView.as_view()),
]
