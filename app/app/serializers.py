from rest_framework.serializers import ModelSerializer

from .models import Webhook


class WebhookSerializer(ModelSerializer):

    class Meta:
        model = Webhook
        exclude = ('recorded_time', )
