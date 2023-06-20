from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    return render(request, 'main/main.html')


def setup(request):
    return render(request, 'main/setup.html')


def monitoring(request):
    if request.user.is_authenticated:
        return render(request, 'main/monitoring.html')
    else:
        return HttpResponseRedirect('authorization/login/')
        