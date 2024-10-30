from rest_framework import viewsets
from .models import Namelist, Playlist
from .serializers import NamelistSerializer, PlaylistSerializer

class NamelistViewSet(viewsets.ModelViewSet):
    queryset = Namelist.objects.all()
    serializer_class = NamelistSerializer

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer