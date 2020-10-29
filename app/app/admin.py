from django.contrib import admin
from django.contrib.postgres import fields
from django_json_widget.widgets import JSONEditorWidget

from app.models import Webhook


class WebhookAdmin(admin.ModelAdmin):
    list_display = ['id', 'recorded_time', 'payload']

    formfield_overrides = {
        fields.JSONField: {'widget': JSONEditorWidget},
    }
    class Meta:
        model = Webhook


admin.site.register(Webhook, WebhookAdmin)