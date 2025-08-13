from django.contrib import admin
from .models import Person, Musician, Album, Runner, Manufacturer, Car, Topping, Pizza
# Register your models here.

app_models = [
    Person,
    Musician,
    Album,
    Runner,
    Manufacturer,
    Car,
    Topping,
    Pizza,
]

admin.site.register(app_models)
