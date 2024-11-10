from django.shortcuts import render
from landing.models import Athlete
# Create your views here.


def temp(request):

    # query = Athlete.objects.get(pk=1)
    # a = list(query)
    return render(request, 'temp.html', {'name': a[1].name})
