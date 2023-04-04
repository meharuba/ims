from django.urls import path
from .views import (
    PurchaseListView, PurchaseDetailView, PurchaseCreateView, PurchaseUpdateView, PurchaseDeleteView,
    SaleListView, SaleDetailView
)

app_name = 'order'

urlpatterns = [
    # Purchase URLs
    path('purchase/', PurchaseListView.as_view(), name='purchase_list'),
    path('purchase/<int:pk>/', PurchaseDetailView.as_view(), name='purchase_detail'),
    path('purchase/create/', PurchaseCreateView.as_view(), name='purchase_create'),
    path('purchase/<int:pk>/update/', PurchaseUpdateView.as_view(), name='purchase_update'),
    path('purchase/<int:pk>/delete/', PurchaseDeleteView.as_view(), name='purchase_delete'),

    # Sale URLs
    path('sale/', SaleListView.as_view(), name='sale_list'),
    path('sale/<int:pk>/', SaleDetailView.as_view(), name='sale_detail'),
]




# from django.urls import path
# from .views import (
#     TransactionListView,
#     TransactionCreateView,
#     TransactionDetailView,
#     TransactionUpdateView,
#     TransactionDeleteView,
#     TransactionLineCreateView,
#     TransactionLineUpdateView,
#     TransactionLineDeleteView,
# )
#
# app_name = 'order'
#
#
# urlpatterns = [
#     path('', TransactionListView.as_view(), name='transaction_list'),
#     path('create/', TransactionCreateView.as_view(), name='transaction_create'),
#     path('<int:pk>/', TransactionDetailView.as_view(), name='transaction_detail'),
#     path('<int:pk>/update/', TransactionUpdateView.as_view(), name='transaction_update'),
#     path('<int:pk>/delete/', TransactionDeleteView.as_view(), name='transaction_delete'),
#     path('<int:pk>/lines/create/', TransactionLineCreateView.as_view(), name='transactionline_create'),
#     path('lines/<int:pk>/update/', TransactionLineUpdateView.as_view(), name='transactionline_update'),
#     path('lines/<int:pk>/delete/', TransactionLineDeleteView.as_view(), name='transactionline_delete'),
# ]

