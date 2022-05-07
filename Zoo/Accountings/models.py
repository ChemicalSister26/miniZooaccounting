from django.db import models

# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=45)
    type = models.CharField(max_length=10)
    predators = models.CharField(max_length=3)
    meal = models.ForeignKey('Meal', on_delete=models.PROTECT, null=True)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name

class Meal(models.Model):
    name = models.CharField(max_length=45)
    cur = models.IntegerField()
    measure = models.CharField(max_length=3)
    type = models.CharField(max_length=10)
    normofconsumption = models.IntegerField()

    def __str__(self):
        return self.name


