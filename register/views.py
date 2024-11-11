from django.shortcuts import render, redirect
from landing.models import Athlete
# Create your views here.


def create_athlete(request):
    if request.method == "GET":
        return render(request, 'templates/surveyinfo.html')

    elif request.method == "POST":
        print(request.body)
        return redirect('servey-sports')


def sport_select(request):
    return render(request, 'templates/surveySports.html')
