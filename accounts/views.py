from django.shortcuts import render
from django.views.generic import *
from .forms import *
from django.urls import reverse_lazy

# Create your views here.
class SignupPageView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")