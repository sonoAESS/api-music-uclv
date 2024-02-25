from django.db import models
from ..music.models import Musica
from django.contrib.auth import get_user

# Create your models here.
class Namelist(models.Model):
    name=models.CharField(max_length=50)
    public=models.BooleanField()
    
class Playlist(models.Model):
    Nlist=models.ManyToManyField(Namelist)
    Song=models.ManyToManyField(Musica)
    
