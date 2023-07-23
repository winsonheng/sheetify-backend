import json
import base64
import io
import pygame
from common.constants import StatusCode
from common.util.json_util import from_query_set
from common.util.gcloud_util import generate_download_signed_url_v4
from django.core.cache import cache
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from songs.models import Song
from users.models import User
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes

# Create your views here.


#@csrf_exempt
@ensure_csrf_cookie
@api_view(['POST'])
@authentication_classes([TokenAuthentication])

def upload_song(request):
    print(request.user.email)
    print(request.auth.key)
    user = Token.objects.get(key=request.auth.key).user

    body = json.loads(request.body)
    song_name = body.get('songName', '')
    song_base64 = body.get('base64', '')
    difficulty = body.get('difficulty', 'Any')
    bpm = body.get('bpm', 0)

    # print(song_base64)

    # play_song(song_base64)
    song_id = save_song(user, song_name, song_base64, difficulty, bpm)
    
    print(song_id)

    return JsonResponse({
        'message': 'Successfully uploaded: ' + song_name
    }, status=StatusCode.OK)


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

def save_song(user, song_name, song_base64, difficulty, bpm):
    print('======================starting to upload=============================')
    song = Song(user=user)
    song.name = song_name
    song.username = user.username
    song.song_original.save(song_name, ContentFile(base64.b64decode(song_base64)))
    song.difficulty = difficulty
    song.bpm = bpm
    song.save()

    # cache.set('song', song)
    print('*****successfully uploaded ' + song_name + ' to GCloud*****')
    print('======================completed   upload=============================')
    return song.id

# TODO: API for delete
def delete_song(user, song_name):
    #song = Song()
    pass


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def get_songs_by_user(request):
    user = Token.objects.get(key=request.auth.key).user
    
    songs = Song.objects.filter(user=user).values()
    
    for song in songs:
        print(song['name'], song['song_original'])
        song['download_link'] = generate_download_signed_url_v4(song['song_original'])
    
    return JsonResponse({
        'songList': from_query_set(songs)
    }, status=StatusCode.OK)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def get_all_songs(request):
    user = Token.objects.get(key=request.auth.key).user
    
    songs = Song.objects.select_related().values()
    
    for song in songs:
        print(song['name'], song['song_original'])
        song['download_link'] = generate_download_signed_url_v4(song['song_original'])
    
    return JsonResponse({
        'songList': from_query_set(songs)
    }, status=StatusCode.OK)
    
    
@csrf_exempt
def upload_transcription(request):
    body = json.loads(request.body)
    song_id = body.get('song_id', '')
    transcription_b64 = body.get('transcription', '')
    
    song = Song.objects.get(pk=song_id)
    song.song_pdf.save(song.name, ContentFile(base64.b64decode(transcription_b64)))
    song.save()
    
    return JsonResponse({
        'message': 'Successfully uploaded transcription for ' + song.name
    }, status=StatusCode.OK)
    