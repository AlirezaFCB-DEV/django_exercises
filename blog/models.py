from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    post_url = models.SlugField()
    content = models.TextField(max_length=800)
    published_date = models.DateTimeField()

    def __str__(self):
        return f"{self.title} : {self.content}"
