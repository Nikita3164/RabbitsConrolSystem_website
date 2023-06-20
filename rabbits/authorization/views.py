from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from . import forms
 
 
class SignUpView(generic.CreateView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'authorization/signup.html'


def login(request, message=None):
    return render(request, 'registration/login.html')


def test(request):
    return render(request, 'authorization/test.html')