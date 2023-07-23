from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import base64
from utils import transcribe_b64

# Create your views here.
@csrf_exempt
@require_POST
def transcribe_song(request):
    try:
        # Get the base64 encoded audio data from the request
        base64_data = request.POST.get('base64_data')
        # Perform transcription
        transcription = transcribe_b64(base64_data)
        # Return the transcription as JSON response
        return JsonResponse({'transcription': transcription})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
