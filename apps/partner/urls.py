from django.urls import path
from . import views
from .views import delete_district
from .views import delete_dealer
from .views import delete_supplier

from .views import edit_dealer



urlpatterns = [

    path('supplier/create/', views.admin_supplier_create, name='create_supplier'),
    path('dealer/create/', views.admin_dealer_create, name='create_dealer'),
    path('district/create/', views.admin_district_create, name='create_district'),
    # path('', views.dashboard, name='dashboard'),
    path('districts/', views.district_list, name='district_list'),
    path('dealers/', views.dealer_list, name='dealer_list'),
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('districts/<int:district_id>/delete/', delete_district, name='delete_district'),
    path('dealers/<int:dealer_id>/delete/', delete_dealer, name='delete_dealer'),
    path('suppliers/<int:supplier_id>/delete/', delete_supplier, name='delete_supplier'),

    path('<int:dealer_id>/edit/', edit_dealer, name='edit_dealer'),
    path('supplier/<int:pk>/edit/', views.edit_supplier, name='edit_supplier'),
    path('district/<int:pk>/edit/', views.edit_district, name='edit_district'),


]
