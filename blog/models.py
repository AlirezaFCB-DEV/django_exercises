from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    post_url = models.SlugField(allow_unicode=True)
    content = models.TextField(max_length=800)
    published_date = models.DateTimeField()

    def __str__(self):
        return f"{self.title} : {self.content}"

class Profile(models.Model) :
    first_name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.first_name} - {self.lastname}"