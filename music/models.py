from django.db import models

class Song(models.Model):
    link=models.URLField()
    title=models.CharField(max_length=500)
    artista=models.CharField(max_length=50)
    album=models.CharField(max_length=50)
    genre=models.CharField(max_length=100)
    duration=models.DurationField()
    
    def __str__(self):
        return self.title

# Create your models here.
