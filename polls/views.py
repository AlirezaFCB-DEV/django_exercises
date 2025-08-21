from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest, Http404
import asyncio

from users.models import Person
from .models import Article

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


def my_404_view(req):
    return render(req, "polls/404.html", status=404)


async def my_async_view(req):
    await asyncio.sleep(10)
    return HttpResponse("Hello World, This is a async view in django")


def article_detail(req, article_id):
    Article = get_object_or_404(Article, pk=article_id)

    return render(req, "polls/articles.html", {"article": Article})
