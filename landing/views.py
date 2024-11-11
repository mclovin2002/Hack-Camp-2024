from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home page.html')


def hostTeam(request):
    return render(request, 'templates/Basketballteam.html')
