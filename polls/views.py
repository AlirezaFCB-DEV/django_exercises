from django.http import HttpResponse, HttpResponseBadRequest

# Create your views here.


def first_view(req):
    return HttpResponse("Hello , This first my view!!")


def my_error_view(req):
    if 5 == 0:
        return HttpResponse("Welcome HAHAHAHA!!")
    else:
        return HttpResponseBadRequest("You Req Is NotVALID!!")
