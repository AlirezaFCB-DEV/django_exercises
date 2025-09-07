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


def dashboard_view(req):
    if not req.user.is_authenticated:
        return JsonResponse({"error": "Login Required"}, status=401)

    if not req.user.is_active:
        return JsonResponse({"error": "Your account is disabled"}, status=403)

    return JsonResponse({"message": "Welcome to your dashboard"})
