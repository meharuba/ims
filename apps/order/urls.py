from django.urls import path
from .views import (
    TransactionListView,
    TransactionCreateView,
    TransactionDetailView,
    TransactionUpdateView,
    TransactionDeleteView,
    TransactionLineCreateView,
    TransactionLineUpdateView,
    TransactionLineDeleteView,
)

app_name = 'order'


urlpatterns = [
    path('', TransactionListView.as_view(), name='transaction-list'),
    path('create/', TransactionCreateView.as_view(), name='transaction-create'),
    path('<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),
    path('<int:pk>/update/', TransactionUpdateView.as_view(), name='transaction-update'),
    path('<int:pk>/delete/', TransactionDeleteView.as_view(), name='transaction-delete'),
    path('<int:pk>/lines/create/', TransactionLineCreateView.as_view(), name='transactionline-create'),
    path('lines/<int:pk>/update/', TransactionLineUpdateView.as_view(), name='transactionline-update'),
    path('lines/<int:pk>/delete/', TransactionLineDeleteView.as_view(), name='transactionline-delete'),
]

