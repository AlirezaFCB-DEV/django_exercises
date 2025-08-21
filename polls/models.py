from django.db import models

# Create your models here.


class Article (models.Model):
    title = models.CharField(max_length=50)
    created = models.DateField()

    def __str__(self):
        return super().__str__()
