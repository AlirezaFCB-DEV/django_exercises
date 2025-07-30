from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path("" , views.index , name="index"),
    path("<int:pk>/" , views.detail , name="detail"),
    path("<int:pk>/result/" , views.result , name="result"),
    path("<int:question_id>/vote/" , views.vote , name="vote"),
]