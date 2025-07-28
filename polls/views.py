# from django.shortcuts import render
from django.http import HttpResponse # ! Not Good Render That Better Than HttpRes
from django.template import loader

from .models import Question
# Create your views here.


def index(req):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list" :  latest_question_list}
    return HttpResponse(template.render(context , req))


def detail(req, question_id):
    return HttpResponse(f"You're looking at question {question_id}")


def result(req, question_id):
    return HttpResponse(f"you're looking at the result of question {question_id}")


def vote(req, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
