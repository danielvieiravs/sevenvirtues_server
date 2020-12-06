from django.contrib import admin

from .models import (
    RatingPersonalDayVirtues,
    RatingVirtues)


class RatingPersonalDayVirtuesAdmin(admin.ModelAdmin):
    list_display = (
        'created_at',
        'comment',
        'rate',
        'user')


admin.site.register(RatingPersonalDayVirtues, RatingPersonalDayVirtuesAdmin)


class RatingVirtuesAdmin(admin.ModelAdmin):
    list_display = (
        'created_at',
        'rate',
        'user')


admin.site.register(RatingVirtues, RatingVirtuesAdmin)
