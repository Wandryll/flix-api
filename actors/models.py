from django.db import models

import uuid

NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BR', 'Brasil'),
   
)


class Actor(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    birthday = models.DateField()
    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES, default='USA')
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'actors_info'