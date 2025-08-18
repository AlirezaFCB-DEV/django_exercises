from django.urls import path

from .views import first_view, my_error_view

urlpatterns = [
    path("", first_view, name="first_view"),
    path("err/", my_error_view, name="my_error_view")
]
