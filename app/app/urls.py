from rest_framework.routers import DefaultRouter

from .views import WebhookAPIView, PublicWebhookAPIView

router = DefaultRouter()
router.register(r'webhook', WebhookAPIView, basename='webhook')
router.register(r'public-webhook', PublicWebhookAPIView, basename='webhook')
urlpatterns = router.urls
