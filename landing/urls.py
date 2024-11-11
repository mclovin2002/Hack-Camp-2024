from django.contrib import admin
from django.urls import path
from landing import views

urlpatterns = [

    path('', views.home),

]
