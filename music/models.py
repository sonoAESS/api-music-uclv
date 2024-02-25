from django.db import models

class Musica(models.Model):
    link=models.URLField()
    title=models.CharField(max_length=500)
    artista=models.CharField(max_length=50)
    album=models.CharField(max_length=50)

# Create your models here.
