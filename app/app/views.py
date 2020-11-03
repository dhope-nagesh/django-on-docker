from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .serializers import WebhookSerializer
from .models import Webhook


class WebhookAPIView(ModelViewSet):
    serializer_class = WebhookSerializer
    queryset = Webhook.objects.all()
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, )


class PublicWebhookAPIView(ModelViewSet):
    serializer_class = WebhookSerializer
    queryset = Webhook.objects.all()
