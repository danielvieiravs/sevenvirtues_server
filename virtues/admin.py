from django.contrib import admin

from .models import (
    Virtues,
    Actions
)


class VirtuesAdmin(admin.ModelAdmin):
    list_display = (
        'created_at',
        'virtue')


admin.site.register(Virtues, VirtuesAdmin)


class ActionsAdmin(admin.ModelAdmin):
    list_display = (
        'action',
        'created_at',
        'virtue')


admin.site.register(Actions, ActionsAdmin)
