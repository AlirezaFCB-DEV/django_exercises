from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest, Http404

from users.models import Person

# Create your views here.


def first_view(req):
    return HttpResponse("Hello , This first my view!!")


def my_error_view(req):
    if 5 == 0:
        return HttpResponse("Welcome HAHAHAHA!!")
    else:
        return HttpResponseBadRequest("You Req Is NotVALID!!")


def persons_details_view(req, person_f_name):
    try:
        person = Person.objects.get(first_name=person_f_name)
    except Person.DoesNotExist:
        raise Http404("User Not Found!!!")

    return render(req, "polls/persons_details.html", {"person": person})
