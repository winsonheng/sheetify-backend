import json
import base64
import io
import pygame
from django.core.cache import cache
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.shortcuts import render
from songs.models import Song
from users.models import User
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

#@csrf_exempt
@ensure_csrf_cookie
def upload_song(request):

    body = json.loads(request.body)
    song_name = body.get('songName', '')
    song_base64 = body.get('base64', '')

    # print(song_base64)

    # play_song(song_base64)
    save_song(song_name, song_base64)

    return HttpResponse('Thanks for uploading ' + song_name)


def play_song(song_base64):
    pygame.mixer.init()
    sound_file_data = base64.b64decode(song_base64)
    #assert sound_file_data.startswith(b'OggS')  # just to prove it is an Ogg Vorbis file
    sound_file = io.BytesIO(sound_file_data)
    # The following line will only work with VALID data. With above example data it will fail.
    sound = pygame.mixer.Sound(sound_file)
    ch = sound.play()
    while ch.get_busy():
        pygame.time.wait(100)

def save_song(song_name, song_base64):
    print('======================starting to upload=============================')
    #song = Song()
    #song.song_base64.save(song_name, ContentFile(song_base64.encode('utf-8')))
    # cache.set('song', song)
    print('***********successfully uploaded ' + song_name + 'to GCloud*************')

def delete_song(user, song_name):
    #song = Song()
    pass