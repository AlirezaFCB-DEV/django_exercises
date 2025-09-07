from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import AnonymousUser

# Create your views here.


def profile_view(req):
    if isinstance(req.user, AnonymousUser):
        return JsonResponse({"error": "You Must Login First!!"}, status=401)
    return JsonResponse({
        "username": req.user.username,
        "email": req.user.email
    })
