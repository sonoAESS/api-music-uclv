from .models import Musica
from rest_framework import serializers

class MusicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Musica
        fields=['link','title','artista','album']