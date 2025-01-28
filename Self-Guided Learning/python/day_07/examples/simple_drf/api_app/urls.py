from rest_framework.routers import DefaultRouter
from .views import MessageViewSet
from rest_framework.documentation import include_docs_urls
from django.urls import path

router = DefaultRouter()
router.register(r"messages", MessageViewSet)

urlpatterns = router.urls
urlpatterns += [path("docs/", include_docs_urls(title="Message API"))]
