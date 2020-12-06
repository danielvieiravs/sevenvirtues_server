from django.db import models

from core.base_models import BaseModel


class DailyTracking(BaseModel):
    user = models.ForeignKey(
        'users.SevenVirtuesUsers', on_delete=models.CASCADE)
    action = models.ForeignKey('virtues.Actions', on_delete=models.CASCADE)
