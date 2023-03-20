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
from apps.partner import views
from apps.partner.views import delete_district
from django.contrib import admin
from apps.partner.views import edit_dealer
from django.urls import path, include



urlpatterns = [
    path('', DashboardView.as_view(), name='index'),
    path('accounts/', include('apps.authentication.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('partner/', include('apps.partner.urls')),
    path('accounts/', include('apps.authentication.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', UserCreationView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('__debug__/', include('debug_toolbar.urls')),
    path('supplier/create/', views.admin_supplier_create, name='create_supplier'),
    path('dealer/create/', views.admin_dealer_create, name='create_dealer'),
    path('district/create/', views.admin_district_create, name='create_district'),
    path('districts/', views.district_list, name='district_list'),
    path('dealers/', views.dealer_list, name='dealer_list'),
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('districts/<int:district_id>/delete/', delete_district, name='delete_district'),
    path('dealers/<int:dealer_id>/delete/', views.delete_dealer, name='delete_dealer'),
    path('suppliers/<int:supplier_id>/delete/', views.delete_supplier, name='delete_supplier'),
    path('<int:dealer_id>/edit/', edit_dealer, name='edit_dealer'),
    path('supplier/<int:pk>/edit/', views.edit_supplier, name='edit_supplier'),
    path('district/<int:pk>/edit/', views.edit_district, name='edit_district'),


    path('catalogue/', include('apps.catalogue.urls')),
    path('order/', include('apps.order.urls')),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]

for static_dir in settings.STATICFILES_DIRS:
    urlpatterns += static(settings.STATIC_URL, document_root=static_dir)

























