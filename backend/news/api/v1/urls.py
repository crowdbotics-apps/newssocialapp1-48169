from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ArticleViewSet, CategoryViewSet, UserArticleViewSet

router = DefaultRouter()
router.register("userarticle", UserArticleViewSet)
router.register("article", ArticleViewSet)
router.register("category", CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
