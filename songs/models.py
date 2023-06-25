from django.db import models
from datetime import datetime

class Song(models.Model):
    
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)

    name = models.CharField(max_length=255)

    upload_date = models.DateTimeField(default=datetime.now, blank=True)

    filepath = models.URLField(default=None, blank=True, null=True)

    song_base64 = models.FileField(upload_to='songs')

    def __str__(self):
        return self.name
