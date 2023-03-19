from django.db import models
from django.urls import reverse


# Create your models here.
class Cabinet(models.Model):
    location = models.TextField()

    def get_absolute_url(self):
        return reverse('cabinets')


class Bottle(models.Model):
    cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE)
    producer = models.TextField()
    production_year = models.DateField()
    volume = models.DecimalField(decimal_places=2, max_digits=4)


