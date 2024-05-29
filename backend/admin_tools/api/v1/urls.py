from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ContentModerationViewSet

router = DefaultRouter()
router.register("contentmoderation", ContentModerationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
