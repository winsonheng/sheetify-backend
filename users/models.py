from django.db import models

# Create your models here.

class User(models.Model):
    
    class VerificationStatus(models.IntegerChoices):
        BLOCKED = 0
        PENDING = 1
        VERIFIED = 2

    name = models.CharField(max_length=255)

    email = models.EmailField()

    password = models.CharField(max_length=255)

    verification_status = models.IntegerField(
        choices=VerificationStatus.choices,
        default=0
    )

    def __str__(self):
        return self.name