from django.conf import settings
from django.db import models


class UserActivity(models.Model):
    "Generated Model"
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="useractivity_user",
    )
    activity_type = models.CharField(
        max_length=50,
    )
    activity_time = models.DateTimeField(
        null=False,
        blank=False,
    )


# Create your models here.
