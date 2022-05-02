from django.db import models

# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=45)
    type = models.CharField(max_length=10)
    predators = models.CharField(max_length=3)
