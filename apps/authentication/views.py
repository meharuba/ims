from django.views.generic import CreateView
from apps.authentication.forms import UserRegistrationForm
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView


class UserCreationView(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('index')

def logout_view(request):
    logout(request)
    return redirect(settings.LOGIN_URL)

