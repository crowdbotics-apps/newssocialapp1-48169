from rest_framework import authentication
from admin_tools.models import ContentModeration
from .serializers import ContentModerationSerializer
from rest_framework import viewsets


class ContentModerationViewSet(viewsets.ModelViewSet):
    serializer_class = ContentModerationSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = ContentModeration.objects.all()
