from django.urls import path
from .views import user_list, update_user , delete_user ,search_users

urlpatterns = [
    path("", user_list, name="user_list"),
    path("update/", update_user, name="update_user"),
    path("delete-user/" , delete_user , name="delete_user"),
    path("search/" , search_users , name="search_users")
]
