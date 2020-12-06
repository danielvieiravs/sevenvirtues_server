from django.contrib import admin

from .models import (
    SevenVirtuesUsers
)


class SevenVirtuesUsersAdmin(admin.ModelAdmin):
    list_display = (
        'date_joined',
        'email')


admin.site.register(SevenVirtuesUsers, SevenVirtuesUsersAdmin)
