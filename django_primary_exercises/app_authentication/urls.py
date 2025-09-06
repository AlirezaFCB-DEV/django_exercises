from django.urls import path

from .views import add_user, login_user, dashboard

app_name = "app_authentication"
urlpatterns = [
    path("add_user/", add_user, name="add_user"),
    path("login/", login_user, name="login_user"),
    path("dashboard/<str:username>/", dashboard, name="dashboard")
]
