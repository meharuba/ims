from django.urls import path
from apps.authentication.views import UserCreationView
from apps.authentication.views import CustomLoginView


urlpatterns = [
    path('signup/', UserCreationView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),

]







