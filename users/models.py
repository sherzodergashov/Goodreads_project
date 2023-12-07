from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(default='default_profile_pic.jpg')
    # address = models.CharField(max_length=200)
    # phone = models.CharField(max_length=17)

