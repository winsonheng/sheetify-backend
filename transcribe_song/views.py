from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import base64
import requests
from transcribe_song.utils import transcribe_b64

POST_URL = 'https://orbital-backend-production.up.railway.app/songs/uploadTranscription/'

# Create your views here.
@csrf_exempt
@require_POST
def transcribe_song(request):
    try:
        # Get the base64 encoded audio data from the request
        base64_data = request.POST.get('base64_data')
        song_id = request.POST.get('song_id')
        # Perform transcription
        transcription = transcribe_b64(base64_data)

        # send POST to server to uplaod transcription
        result = {'transcription': transcription, 'song_id': song_id}
        requests.post(POST_URL, json = result)
        # Return the transcription as JSON response
        return JsonResponse(result)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
