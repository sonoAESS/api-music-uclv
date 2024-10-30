from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from music.views import SongSearch
from playlist.views import NamelistViewSet, PlaylistViewSet  # Cambia a las vistas

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path(
        "api/token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        "api/token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"
    ),
    path("api/search/", SongSearch.as_view(), name="search"),
    # Rutas para las playlists
    path(
        "api/playlists/",
        PlaylistViewSet.as_view({"get": "list", "post": "create"}),
        name="playlist-list",
    ),  # Listar y crear playlists
    path(
        "api/playlists/<int:pk>/",
        PlaylistViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="playlist-detail",
    ),  # Obtener, actualizar y eliminar una playlist
    # Rutas para las namelists
    path(
        "api/namelists/",
        NamelistViewSet.as_view({"get": "list", "post": "create"}),
        name="namelist-list",
    ),  # Listar y crear namelists
    path(
        "api/namelists/<int:pk>/",
        NamelistViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="namelist-detail",
    ),  # Obtener, actualizar y eliminar una namelist
]
