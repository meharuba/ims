from django.urls import path
from apps.authentication.views import UserCreationView, UserLogoutView


urlpatterns = [
    path('accounts/signup/', UserCreationView.as_view(), name='signup'),
    path('accounts/logout/', UserLogoutView.as_view(next_page='login'), name='logout'),

]

