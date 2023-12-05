from django.db import models

import uuid

from genres.models import Genre
from actors.models import Actor


class Movie(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=200)
    genre = models.ManyToManyField(Genre, related_name='movies')
    minumum_age = models.IntegerField()
    release_date = models.DateField()
    actors = models.ManyToManyField(Actor, related_name='movies')
    resume = models.TextField(max_length=400)
    image = models.ImageField(upload_to='media/movies_img')
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'movies'