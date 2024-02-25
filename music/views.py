from django.shortcuts import render
from rest_framework import permissions,generics,filters
from .serializers import MusicSerializer
from .models import Musica

class MusicSearch(generics.ListAPIView):
    queryset=Musica.objects.all()
    serializer_class=MusicSerializer
    permission_classes=[permissions.IsAuthenticated]
    filter_backends=[filters.SearchFilter]
    search_fields = ['$title','$artista','$album']



# Create your views here.
