from django.contrib import admin

# Register your models here.

from .models import *

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cur', 'measure', 'type', 'normofconsumption')

admin.site.register(Animal)




admin.site.register(Meal)