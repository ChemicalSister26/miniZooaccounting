from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
# Create your views here.

from django.views.generic import ListView, DetailView
from rest_framework import generics

from Accountings.models import *
from Accountings.serializers import AnimalSerializer, MealSerializer


class AnimalView(ListView):
    template_name = 'Accountings/index.html'
    model = Animal
    context_object_name = 'post'

class MealView(ListView):
    template_name = 'Accountings/meal.html'
    model = Meal
    context_object_name = 'meal'


class AnimalAPIGet(generics.ListAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

class AnimalAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

class MealAPIGet(generics.ListAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

class MealAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer