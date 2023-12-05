from django.db import models

import uuid


class Genre(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'genres'