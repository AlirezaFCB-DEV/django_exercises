from django.db import models

# Create your models here.


class Person(models.Model):
    SHIRT_SIZES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
        ("XL", "XLarge"),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    shirt_size = models.CharField(max_length=2, choices=SHIRT_SIZES)

    def __str__(self):
        return self.first_name


class Musician(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_start = models.IntegerField()


class Runner(models.Model):
    MedalType = models.TextChoices("MedalType", "Gold Silver Bronze")
    name = models.CharField(max_length=60)


#!! RelationShips

# ? Many To One
class Manufacturer(models.Model):
    # * ...
    pass


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    # * ...
    pass

# ? Many To Many


class Topping(models.Model):
    # * ...
    pass


class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping)
    pass


# ? Extra fields on many-to-many relationships

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through="Membership")

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["person", "group"],
                name="unique_person_group")
        ]

# ? One To One


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)


class Restaurant (models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE)
    serves_pizza = models.BooleanField(default=False)
