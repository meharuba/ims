from django import forms
from .models import Transaction, TransactionLine

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['date', 'dealer', 'supplier', 'transaction_type']
        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'dealer': forms.Select(attrs={'class': 'form-control'}),
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'transaction_type': forms.Select(attrs={'class': 'form-control'}),
        }

class TransactionLineForm(forms.ModelForm):
    class Meta:
        model = TransactionLine
        fields = ['transaction', 'product', 'quantity', 'price']
        widgets = {
            'transaction': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }

