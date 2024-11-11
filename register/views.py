from django.shortcuts import render, redirect
from landing.models import Athlete
# Create your views here.


def create_athlete(request):
    if request.method == "GET":
        return render(request, 'templates/surveyinfo.html')

    elif request.method == "POST":
        print(request.body)
        return redirect('survey-sports')


def sport_select(request):
    return render(request, 'templates/surveySports.html')


def basketball(request):
    if request.method == "GET":
        return render(request, 'templates/SurveyBasketball.html')

    elif request.method == "POST":
        print(request.body)
        return redirect('/')


def tennis(request):
    if request.method == "GET":
        return render(request, 'templates/surveyTennis.html')

    elif request.method == "POST":
        print(request.body)
        return redirect('/')
