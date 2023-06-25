from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    
    class VerificationStatus(models.IntegerChoices):
        BLOCKED = 0
        PENDING = 1
        VERIFIED = 2

    username = models.CharField(max_length=255, unique=True, null=True)

    email = models.EmailField(max_length=255, unique=True)

    password = models.CharField(max_length=255)

    verification_status = models.IntegerField(
        choices=VerificationStatus.choices,
        default=0
    )

    last_login = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name