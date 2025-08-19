from django.urls import path

from .views import first_view, my_error_view, persons_details_view , my_404_view , my_async_view

urlpatterns = [
    path("", first_view, name="first_view"),
    path("err/", my_error_view, name="my_error_view"),
    path("users/<str:person_f_name>/", persons_details_view,  name="persons_details_view"),
    path("404/" , my_404_view , name="404_error"),
    path("async/" , my_async_view , name="async_view")
]
