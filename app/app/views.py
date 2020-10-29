import json

from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.views import APIView

from .models import Webhook


class WebhookAPIView(APIView):

    def post(self, *args, **kwargs):

        payload = self.request.data

        Webhook.objects.create(payload=payload)

        return Response(status=HTTP_201_CREATED)

