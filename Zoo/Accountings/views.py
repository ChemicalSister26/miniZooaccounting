from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
# Create your views here.

from django.views.generic import ListView, DetailView

from Accountings.models import *


class AnimalView(ListView):
    template_name = 'Accountings/index.html'
    model = Animal
    context_object_name = 'post'

class MealView(ListView):
    template_name = 'Accountings/meal.html'
    model = Meal
    context_object_name = 'meal'



