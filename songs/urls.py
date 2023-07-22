from django.urls import path

from . import views

urlpatterns = [
    path("uploadSong/", views.upload_song, name="upload_song"),
    path("getSongsByUser/", views.get_songs_by_user, name="get_songs_by_user")
]