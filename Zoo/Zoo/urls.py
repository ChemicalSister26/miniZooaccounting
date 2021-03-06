"""Zoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.views.generic import TemplateView

from Accountings.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', AnimalView.as_view()),
    path('meal/', MealView.as_view()),
    path('API/animals/', AnimalAPIGet.as_view()),
    path('API/meal/', MealAPIGet.as_view()),
    path('API/animals/<int:pk>/', AnimalAPI.as_view()),
    path('API/meal/<int:pk>/', MealAPI.as_view()),
]
