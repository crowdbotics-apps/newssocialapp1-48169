from django.conf import settings
from django.db import models


class UserArticle(models.Model):
    "Generated Model"
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="userarticle_user",
    )
    article = models.ForeignKey(
        "news.Article",
        on_delete=models.CASCADE,
        related_name="userarticle_article",
    )
    saved = models.BooleanField(
        default="False",
    )
    read_later = models.BooleanField(
        default="False",
    )


class Article(models.Model):
    "Generated Model"
    title = models.CharField(
        max_length=255,
    )
    content = models.TextField()
    category = models.CharField(
        max_length=100,
    )
    published_date = models.DateTimeField(
        null=True,
        blank=True,
    )
    author = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    is_trending = models.BooleanField(
        default="False",
    )
    image = models.ImageField(
        null=True,
        blank=True,
    )


class Category(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=100,
    )


# Create your models here.
