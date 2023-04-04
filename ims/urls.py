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
from django.conf.urls.static import static
from apps.index_view import DashboardView
from apps.authentication.views import UserCreationView
from apps.authentication.views import CustomLoginView
from apps.authentication.views import logout_view
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', DashboardView.as_view(), name='index'),
    path('accounts/', include('apps.authentication.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('signup/', UserCreationView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('__debug__/', include('debug_toolbar.urls')),

    path('partner/', include('apps.partner.urls')),
    path('quotation/', include('apps.quotation.urls')),

    path('catalogue/', include('apps.catalogue.urls')),
    path('order/', include('apps.order.urls')),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]

for static_dir in settings.STATICFILES_DIRS:
    urlpatterns += static(settings.STATIC_URL, document_root=static_dir)

























