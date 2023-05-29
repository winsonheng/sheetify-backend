from django.urls import path

from . import views

urlpatterns = [

    path("uploadSong/", views.upload_song, name="upload_song"),

]