from django.shortcuts import render , HttpResponse

# Create your views here.

def test_view (req) :
    return HttpResponse("Hello I'm Test View In Django")