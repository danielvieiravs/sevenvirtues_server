from django.db import models

from . import choices

from core.base_models import BaseModel


class Virtues(BaseModel):
    virtue = models.PositiveIntegerField(
        choices=choices.VIRTUES_CHOICES,
        default=choices.VIRTUE_CHARITY)
    description = models.TextField(
        blank=True,
        null=True)

    def __str__(self):
        return str(self.get_virtue_display())


class Actions(BaseModel):
    virtue = models.ForeignKey('virtues.Virtues', on_delete=models.CASCADE)
    action = models.TextField()

    def __str__(self):
        return str(self.action)
