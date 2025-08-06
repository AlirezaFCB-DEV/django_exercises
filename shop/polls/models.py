from mongoengine import Document , StringField , IntField , DateTimeField
# Create your models here.

class User (Document) :
    name = StringField(required=True , max_length=50)
    age = IntField(required=True , max_value=100)
    email = StringField(required=True , max_length=100)
    create_at = DateTimeField()