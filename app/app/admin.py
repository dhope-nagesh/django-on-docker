from django.contrib import admin
from django.contrib.postgres import fields
from django_json_widget.widgets import JSONEditorWidget
from rest_framework.authtoken.admin import TokenAdmin

from app.models import Webhook


TokenAdmin.raw_id_fields = ['user']


class WebhookAdmin(admin.ModelAdmin):
    list_display = ['id', 'recorded_time', 'payload']

    formfield_overrides = {
        fields.JSONField: {'widget': JSONEditorWidget},
    }

    class Meta:
        model = Webhook


admin.site.register(Webhook, WebhookAdmin)
