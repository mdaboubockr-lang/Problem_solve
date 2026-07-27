from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.


class UserCreation(CreateView):
    form_class = UserCreationForm
    model = User
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')