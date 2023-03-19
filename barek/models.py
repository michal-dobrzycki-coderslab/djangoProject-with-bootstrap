from django.db import models
from django.urls import reverse


# Create your models here.
class Cabinet(models.Model):
    location = models.TextField()

    def get_absolute_url(self):
        return reverse('cabinets')

    def __str__(self):
        return self.location


class Bottle(models.Model):
    cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE)
    producer = models.TextField()
    production_year = models.DateField()
    volume = models.DecimalField(decimal_places=2, max_digits=4)

    def get_absolute_url(self):
        return reverse('cabinets')

    def __str__(self):
        return f"{self.producer}, z roku {self.production_year}. Pojemność: {self.volume}"
