from rest_framework import serializers
from .models import Namelist, Playlist

class NamelistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Namelist
        fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'