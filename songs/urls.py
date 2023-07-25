from django.urls import path

from . import views

urlpatterns = [
    path("uploadSong/", views.upload_song, name="upload_song"),
    path("getSongsByUser/", views.get_songs_by_user, name="get_songs_by_user"),
    path("getAllSongs/", views.get_all_songs, name="get_all_songs"),
    path("uploadTranscription/", views.upload_transcription, name='upload_transcription'),
    path("updateGcloudCors/", views.update_gcloud_cors, name="update_gcloud_cors")
]