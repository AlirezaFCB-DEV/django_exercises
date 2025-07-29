from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question, Choice
# Create your views here.


def index(req):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list":  latest_question_list}
    return render(req, "polls/index.html", context)


def detail(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(req, "polls/detail.html", {"question": question, "req": req})


def result(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(req, "polls/result.html", {"question": question})


def vote(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=req.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        #! Redisplay the question voting form.
        return render(
            req,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice."
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        #! Always return an HttpResponseRedirect after successfully dealing
        #! with POST data. This prevents data from being posted twice if a
        #! user hits the Back button.
        return HttpResponseRedirect(reverse("polls:result", args=(question.id,)))
