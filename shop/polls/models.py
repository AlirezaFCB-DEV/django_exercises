from mongoengine import Document, StringField, IntField, DateTimeField
from datetime import datetime
# Create your models here.


class User (Document):
    name = StringField(required=True, max_length=50)
    age = IntField(required=True, max_value=100)
    email = StringField(required=True, max_length=100)
    created_at = DateTimeField(default=datetime.now())
