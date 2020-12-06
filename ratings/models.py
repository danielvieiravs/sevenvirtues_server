from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from core.base_models import BaseModel


class RatingVirtues(BaseModel):
    user = models.ForeignKey(
        'users.SevenVirtuesUsers', on_delete=models.CASCADE)
    rate = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(7)])


class RatingPersonalDayVirtues(BaseModel):
    user = models.ForeignKey(
        'users.SevenVirtuesUsers', on_delete=models.CASCADE)
    rate = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    comment = models.TextField()
