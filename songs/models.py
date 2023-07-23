import pytz
from django.db import models
from django.utils import timezone
from datetime import datetime

class Song(models.Model):
    
    class DifficultyLevel(models.TextChoices):
        EASY = 'Easy'
        MEDIUM = 'Medium'
        HARD = 'Hard'
        EXTREME = 'Extreme'
    
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    
    username = models.CharField(max_length=255, unique=True, null=True)

    name = models.CharField(max_length=255)

    upload_date = models.DateTimeField(default=timezone.now, blank=True)
    
    difficulty = models.CharField(
        choices=DifficultyLevel.choices,
        max_length=20,
        blank=True
    )
    
    bpm = models.IntegerField(blank=True, null=True)

    # not required since it is only generated during getSongs request
    # download_link = models.URLField(default=None, blank=True, null=True)

    song_original = models.FileField(upload_to='songs/original', default=None)
    
    song_pdf = models.FileField(upload_to='songs/pdf', default=None, blank=True, null=True)
    
    song_musescore = models.FileField(upload_to='songs/musescore', default=None, blank=True, null=True)

    def __str__(self):
        return self.name
