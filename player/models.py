from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Player(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, default='profile_pictures/fallback.png')
    rank = models.IntegerField(default=1000)
    phone_number = PhoneNumberField(blank=True, null=True)
    win = models.IntegerField(default=0)
    lose = models.IntegerField(default=0)
    nickname = models.CharField(blank=True, null=True, max_length=30)
    def __str__(self):
        return self.username
    



