from django.urls import path, register_converter

from .views import first_view, my_error_view, persons_details_view, my_404_view, my_async_view, article_detail, article_year


class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)


register_converter(FourDigitYearConverter, "yyyy")


urlpatterns = [
    path("", first_view, name="first_view"),
    path("err/", my_error_view, name="my_error_view"),
    path("users/<str:person_f_name>/", persons_details_view,
         name="persons_details_view"),
    path("404/", my_404_view, name="404_error"),
    path("async/", my_async_view, name="async_view"),
    path("articles/<int:article_id>/", article_detail, name="article_detail"),
    path("articles/year/<yyyy:year>/", article_year)

]
