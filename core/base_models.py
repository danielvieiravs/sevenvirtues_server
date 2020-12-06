from datetime import datetime

from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(default=datetime.utcnow, db_index=True)

    class Meta:
        abstract = True
