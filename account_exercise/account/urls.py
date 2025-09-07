from django.urls import path
from . import views

app_name = "account"
urlpatterns = [
    path("", views.dashboard_view, name="dashboard"),
    path("profile/", views.profile_view, name="profile_view"),
    path("user_detail/<int:user_id>/", views.user_detail, name="user_detail"),
    path("reports/", views.report_view, name="report_view"),
    # path("login/", views.login, name="login")
]
