from django.db import models
from django.utils import timezone
# Create your models here.


#  Allow a user to sumbit the car's make, model, year, and mpg (miles per gallon).
class NewCarModel(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField(default=0)
    mpg = models.IntegerField(default=0)

    def __str__(self):
        return self.make + ' ' + self.model