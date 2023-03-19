from django.shortcuts import render
from django.views.generic import ListView, CreateView

from barek.models import Cabinet


# Create your views here.
class CabinetListView(ListView):
    model = Cabinet


class CreateCabinetView(CreateView):
    model = Cabinet
    fields = ['location']