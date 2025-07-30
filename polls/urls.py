from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path("" , views.IndexView.as_view() , name="index"),
    path("<int:pk>/" , views.Detail_View.as_view() , name="detail"),
    path("<int:pk>/result/" , views.Result_View.as_view() , name="result"),
    path("<int:question_id>/vote/" , views.vote , name="vote"),
]