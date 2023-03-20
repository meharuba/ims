from django.views.generic import CreateView
from apps.authentication.forms import UserRegistrationForm
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

class UserCreationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')


