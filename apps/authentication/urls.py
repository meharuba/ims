from django.urls import path

from apps.authentication.views import UserCreationView


urlpatterns = [
    path('accounts/signup/', UserCreationView.as_view(), name='signup'),
]

