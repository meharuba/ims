"""ims URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from apps.index_view import DashboardView

urlpatterns = [
    path('', DashboardView.as_view(), name='index'),
    # path('oder/', include('apps.order.urls')),
    # path('quotation/', include('apps.quotation.urls')),
    # path('partner/', include('apps.partner.urls')),
    # path('catalogue/', include('apps.catalogue.urls')),
    path('accounts/', include('apps.authentication.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('admin/', admin.site.urls),


    # path('', MyLoginView.as_view(), name='login'),
    # path('dashboard/', login_required(TemplateView.as_view(template_name='dashboard.html')), name='dashboard'),
    # path('accounts/', include('django.contrib.auth.urls')),
    #






]









