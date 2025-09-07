from django.db import models
from django.contrib.auth.models import AbstractUser, User, Group, Permission
# Create your models here.


class Custom_User (AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True
    )

    class Meta:
        permissions = [
            ("can_view_reports", "Can view system reports"),
        ]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    age = models.IntegerField(null=True, blank=True)
