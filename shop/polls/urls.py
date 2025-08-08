from django.urls import path
from .views import show_users, update_user, delete_user, search_users

urlpatterns = [
    path("", show_users, name="show_users"),
    path("update/", update_user, name="update_user"),
    path("delete-user/", delete_user, name="delete_user"),
    path("search/", search_users, name="search_users")
]
