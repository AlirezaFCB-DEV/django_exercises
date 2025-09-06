from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import Add_User, Login_User

# Create your views here.
# from django.contrib.auth import logout

# logout(request)  # logout method


def add_user(req):
    if req.method == "POST":
        form = Add_User(req.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(
                    form.cleaned_data["username"], form.cleaned_data["email"], form.cleaned_data["password"])
                user.save()
            except:
                raise ValueError("This Is Not Valid")

    else:
        form = Add_User()
    return render(req, "auth/add_user_form.html", {"form": form})


def login_user(req):
    if req.method == "POST":
        form = Login_User(req.POST)
        if form.is_valid():
            user = authenticate(
                req, username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                login(req,  user)
            else:
                raise ValueError("Login Or Password Incorrect!!")
    else:
        form = Login_User()

    return render(req, "auth/login.html", {"form": form})


@login_required
def dashboard(req, username):
    try:
        user_profile = User.objects.get(username=username)
        return render(req, "auth/dashboard.html", {"user": user_profile})
    except User.DoesNotExist:
        return redirect("app_authentication:login_user")
