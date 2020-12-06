from django.contrib import admin

from .models import (
    DailyTracking
)


class DailyTrackingAdmin(admin.ModelAdmin):
    list_display = (
        'created_at',
        'user',
        'action',
        'virtue')

    def virtue(self, obj):
        return obj.action.virtue


admin.site.register(DailyTracking, DailyTrackingAdmin)
