from rest_framework import serializers
from news.models import Article, Category, UserArticle


class UserArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserArticle
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
