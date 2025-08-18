from django.shortcuts import HttpResponse

# Create your views here.

def first_view (req) :
    return HttpResponse("Hello , This first my view!!")