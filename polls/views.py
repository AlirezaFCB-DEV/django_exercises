# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(req) :
    return HttpResponse("Hi Im Index Func")

def detail(req , question_id):
    return HttpResponse(f"You're looking at question {question_id}")

def result (req , question_id):
    return HttpResponse(f"you're looking at the result of question {question_id}")

def vote(req , question_id) :
    return HttpResponse(f"You're voting on question {question_id}")

