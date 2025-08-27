from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import Add_User

# Create your views here.


def add_user(req):
    if req.method == "POST":
        form = Add_User(req.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(
                    form.cleaned_data["username"], form.cleaned_data["email"], form.cleaned_data["password"])
                user.save()
            except :
                raise ValueError("This Is Not Valid" )

    else:
        form = Add_User()
    return render(req, "auth/add_user_form.html", {"form": form})
