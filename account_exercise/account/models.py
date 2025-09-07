from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Custom_User (AbstractUser):
    class Meta:
        permissions = [
            ("can_view_reports" , "Can view system reports")
        ]