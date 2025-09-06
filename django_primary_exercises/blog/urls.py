from django.urls import path
from . import views

urlpatterns = [
    path("posts", views.post_list, name="post_list"),
    path("posts/<str:post_url>/", views.post_detail, name="post_detail"),
    path("add_post/", views.add_post , name="add_post")
]
