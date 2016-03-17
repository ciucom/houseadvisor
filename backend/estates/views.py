from django.shortcuts import render

from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView

from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Estate

# Create your views here.


class EstateList(ListView):
    model = Estate
    fields = ['title', 'description', 'price', 'image']


class EstateDetail(DetailView):
    model = Estate


class EstateCreation(CreateView):
    model = Estate
    success_url = reverse_lazy('estates:list')
    fields = ['title', 'description', 'price', 'image']


class EstateUpdate(UpdateView):
    model = Estate
    success_url = reverse_lazy('estates:list')
    fields = ['title', 'description', 'price', 'image']


class EstateDelete(DeleteView):
    model = Estate
    success_url = reverse_lazy('estates:list')
