from django.db import models

# Create your models here.
class Person(models.Model) :
    SHIRT_SIZES= [
        ("S" , "Small"),
        ("M" , "Medium"),
        ("L" , "Large"),
        ("XL" , "XLarge"),
    ]
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    shirt_size = models.CharField(max_length=2 , choices=SHIRT_SIZES) 
    

class Musician(models.Model) :
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    
class Album(models.Model):
    artist = models.ForeignKey(Musician , on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_start = models.IntegerField()
    
    
class Runner(models.Model) :
    MedalType = models.TextChoices("MedalType" , "Gold Silver Bronze")
    name = models.CharField(max_length=60)
    