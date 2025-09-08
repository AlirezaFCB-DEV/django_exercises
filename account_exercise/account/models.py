from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.


class Custom_User (AbstractUser):
    phone = models.CharField("phone_number" , max_length=20 , blank=True)
    birth_date = models.DateField("birth" , null=True , blank=True)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    age = models.IntegerField(null=True, blank=True)
