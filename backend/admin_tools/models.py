from django.conf import settings
from django.db import models


class ContentModeration(models.Model):
    "Generated Model"
    article = models.ForeignKey(
        "news.Article",
        on_delete=models.CASCADE,
        related_name="contentmoderation_article",
    )
    status = models.CharField(
        max_length=50,
    )
    moderated_by = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="contentmoderation_moderated_by",
    )
    moderation_time = models.DateTimeField(
        null=True,
        blank=True,
    )


# Create your models here.
