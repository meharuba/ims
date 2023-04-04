from django.urls import path
from .views import QuotationList, QuotationDetail, QuotationCreate, QuotationUpdate, QuotationDelete

app_name = 'quotation'

urlpatterns = [
    path('', QuotationList.as_view(), name='quotation_list'),
    path('<int:pk>/', QuotationDetail.as_view(), name='quotation_detail'),
    path('new/', QuotationCreate.as_view(), name='quotation_create'),
    path('<int:pk>/edit/', QuotationUpdate.as_view(), name='quotation_update'),
    path('<int:pk>/delete/', QuotationDelete.as_view(), name='quotation_delete'),
]
