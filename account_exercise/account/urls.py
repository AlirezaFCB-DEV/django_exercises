from django.urls import path
from . import views

app_name = "account"
urlpatterns = [
    path("", views.dashboard_view, name="profile_view"),
    path("profile/", views.profile_view, name="profile_view"),
    # path("login/", views.login, name="login")
]
