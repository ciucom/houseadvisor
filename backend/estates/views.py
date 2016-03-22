from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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


def authentication(request):
    if request.method == 'POST':
        action = request.POST.get('action', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if action == 'signup':
            user = User.objects.create_user(
                username=username, password=password
            )
            user.save()
        elif action == 'login':
            user = authenticate(username=username, password=password)
            login(request, user)
        return redirect('../')

    return render(request, 'estates/login.html', {})


@method_decorator(login_required(login_url='login/'), name='dispatch')
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
