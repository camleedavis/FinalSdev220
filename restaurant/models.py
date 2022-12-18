from django.db import models

# Create your models here.
class Meals(models.Model):
    mealname = models.CharField(max_length=250, null = False)
    prices = models.FloatField(max_length=20, null = False)
    
    def __str__(self):
        return self.mealname