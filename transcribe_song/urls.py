from django.urls import path
from . import views

urlpatterns = [
    path('', views.transcribe_song, name='transcribe_song'),
]
