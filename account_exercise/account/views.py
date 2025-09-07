from django.shortcuts import render
from django.http import JsonResponse, Http404
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model

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


User = get_user_model()


def user_detail(req, user_id):
    if not req.user.is_authenticated:
        return JsonResponse({"error": "Login Required"}, status=401)

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise Http404("User not found!!")

    if req.user != user:
        return JsonResponse({"error": "Permission denied"}, status=403)

    return JsonResponse({"username": user.username, "email": user.email})
