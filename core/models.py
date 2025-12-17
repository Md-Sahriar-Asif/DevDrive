from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    profile_pic = models.ImageField(upload_to="p_img/", null=True, blank=True)
    address = models.CharField(max_length=120, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    role = models.CharField(max_length=40, null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="following", blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username",)

    def __str__(self):
        return self.email