from datetime import datetime

from .models import User
# Create your views here.

user = User(
    name="Alireza",
    age= 16,
    email= "alirezadeveloper5@gmail.com",
    created_at = datetime.utcnow()
)

user.save()