from django.db import models
from datetime import datetime

class Song(models.Model):
    
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    name = models.TextField()

    upload_date = models.DateField(default=datetime.now, blank=True)

    filepath = models.URLField(default=None, blank=True, null=True)

    song_base64 = models.FileField(upload_to='blobs')

    def __str__(self):
        return self.name


class User(models.Model):

    name = models.TextField()

    def __str__(self):
        return self.name