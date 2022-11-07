from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question


def index(request):
    latest_quesyion_list =  Question.objects.all()
    return render(request, "polls/index.html",{
        "latest_quesyion_list": latest_quesyion_list
    })

def detail(request, question_id):
    return HttpResponse(f"Estás viendo la pregunta número {question_id}")

def results(request, question_id):
    return HttpResponse(f"Estás viendo los resultados de la pregunta número {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Estas votando a la pregunta número {question_id}")