from rest_framework import serializers
from admin_tools.models import ContentModeration


class ContentModerationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentModeration
        fields = "__all__"
