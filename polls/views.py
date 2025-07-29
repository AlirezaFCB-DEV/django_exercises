from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question
# Create your views here.


def index(req):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list":  latest_question_list}
    return render(req, "polls/index.html", context)


def detail(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(req, "polls/detail.html", {"question": question, "req": req})


def result(req, question_id):
    return HttpResponse(f"you're looking at the result of question {question_id}")


def vote(req, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
