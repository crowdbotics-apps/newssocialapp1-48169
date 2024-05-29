from rest_framework import authentication
from news.models import UserArticle, Article, Category
from .serializers import ArticleSerializer, CategorySerializer, UserArticleSerializer
from rest_framework import viewsets


class UserArticleViewSet(viewsets.ModelViewSet):
    serializer_class = UserArticleSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = UserArticle.objects.all()


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Article.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Category.objects.all()
