from django.shortcuts import render
from rest_framework import permissions,generics,filters
from .serializers import SongSerializer
from .models import Song

class SongSearch(generics.ListAPIView):
    queryset=Song.objects.all()
    serializer_class=SongSerializer
    permission_classes=[permissions.IsAuthenticated]
    filter_backends=[filters.SearchFilter]
    search_fields = ['$title','$artista','$album']



# Create your views here.
