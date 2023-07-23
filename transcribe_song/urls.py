from django.urls import path
from . import views

urlpatterns = [
    path("transcribe_song/", views.transcribe_song, name="transcribe_song"),
]
