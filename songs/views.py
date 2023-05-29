import json
from django.http import HttpResponse
from django.shortcuts import render
from songs.models import Song, User
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.

@ensure_csrf_cookie
def upload_song(request):

    
    song_name = request.POST.get('songName', '')
    return HttpResponse("Hello, world. You're at the songs/addSongs index.")
