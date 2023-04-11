from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import     Questions,Choice
from django.http import Http404

# Create your views here.
def index(request):
    latest_question_list = Questions.objects.order_by("-publish_date")[:5]
    template = loader.get_template("polls_app3/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    try:
        question = Questions.objects.get(pk=question_id)
    except Questions.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls_app3/detail.html", {"question": question})

# Create your views here.
def detail(request,question_id):
    return HttpResponse("you are looking at question %s" % question_id)


def results(request,question_id):
    response="you are looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("you are voting on question %s" % question_id)
