from django.http import HttpResponse
from datetime import datetime
# Create your views here.
from .models import User


def user_list(req):
    users = User.objects()
    output = ""

    for user in users:
        output += f"<p>{user.name} - {user.email} - {user.age}</p>"

    return HttpResponse(output)


def update_user(req):
    user = User.objects(name="Alireza").first()
    if user:
        user.age = 17
        user.created_at = datetime.utcnow()
        user.save()
        return HttpResponse("user updated successfully")
    else:
        return HttpResponse("UserNot Found ")


def delete_user(req):
    user = User.objects(name="Alireza").first()

    if user:
        user.delete()
        return HttpResponse("user deleted successfully")
    else:
        return HttpResponse("user not found")


def search_users(req):
    results = User.objects(age__gte=15)
    output = ""

    for user in results:
        output += f"<p>{user.name} - {user.age} : {user.email} - {user.created_at}</p>"

    return HttpResponse(output)
