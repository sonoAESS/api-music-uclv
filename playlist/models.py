from django.db import models
from django.contrib.auth.models import User
from music.models import Song  

class Namelist(models.Model):
    name = models.CharField(max_length=50)
    public = models.BooleanField(default=False)  
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='namelists')

    def __str__(self):
        return self.name


class Playlist(models.Model):
    namelist = models.ForeignKey(Namelist, on_delete=models.CASCADE, related_name='playlists')
    created = models.DateTimeField(auto_now_add=True)
    songs = models.ManyToManyField(Song, related_name='playlists')  

    def __str__(self):
        return f"Playlist de {self.namelist.name}"