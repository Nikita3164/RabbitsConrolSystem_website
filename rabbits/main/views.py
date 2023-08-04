from django.shortcuts import render
from django.http import HttpResponseRedirect
from .apps import get_rabbits 
from .models import Rabbit


def index(request):
    return render(request, 'main/main.html')


def setup(request):
    return render(request, 'main/setup.html')


def monitoring(request):
    if request.user.is_authenticated:
        rabbits = Rabbit.objects.all()
        print(rabbits)
        return render(request, 'main/monitoring.html', { 'rabbits': rabbits })
    else:
        return HttpResponseRedirect('authorization/login/')


def profile(request):
    return render(request, 'main/profile.html')
        