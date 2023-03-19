from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView

from barek.models import Cabinet, Bottle


# Create your views here.
class CabinetListView(ListView):
    model = Cabinet


class CreateCabinetView(CreateView):
    model = Cabinet
    fields = ['location']


class CabinetDetailView(DetailView):
    model = Cabinet


class CreateBottleView(CreateView):
    model = Bottle
    fields = ['cabinet', 'producer', 'production_year', 'volume']
