from django.contrib import admin
from django.urls import path
from register import views

urlpatterns = [
    path('', views.create_athlete),
    path('sports/', views.sport_select, name='survey-sports'),
]
