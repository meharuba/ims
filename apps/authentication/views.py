from django.views.generic import CreateView

from apps.authentication.forms import UserRegistrationForm


class UserCreationView(CreateView):
    form_class = UserRegistrationForm

