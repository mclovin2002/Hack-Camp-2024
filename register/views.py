from django.shortcuts import render, redirect
from landing.models import Athlete
# Create your views here.


def create_athlete(request):
    if request.method == "GET":
        return render(request, 'templates/surveyinfo.html')

    elif request.method == "POST":
        print(request.body)
        form_first_name = request.POST.get('first-name')
        form_last_name = request.POST.get('last-name')
        form_email = request.POST.get('email')
        form_birth_date = request.POST.get('birthdate')
        form_gender = request.POST.get('gender')

        athlete = Athlete.objects.create(
            first_name = form_first_name,
            last_name = form_last_name,
            email = form_email,
            birth_date = form_birth_date,
            gender = form_gender,
        )



        return redirect('survey-sports')



def sport_select(request):
    return render(request, 'templates/surveySports.html')
