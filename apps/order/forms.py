from django import forms
from django.forms.models import inlineformset_factory
from .models import Transaction, TransactionLine
from apps.quotation.models import Quotation, QuotationLine


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['date', 'supplier']


class TransactionLineForm(forms.ModelForm):
    class Meta:
        model = TransactionLine
        fields = ['product', 'quantity', 'price']

    def save(self, commit=True, created_by=None):
        instance = super().save(commit=False)
        if created_by:
            instance.created_by = created_by
        if commit:
            instance.save()
        return instance


TransactionLineFormSet = inlineformset_factory(Transaction, TransactionLine, form=TransactionLineForm, extra=1)


class SaleForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = '__all__'


class QuotationLineForm(forms.ModelForm):
    class Meta:
        model = QuotationLine
        fields = ['product', 'quantity', 'price']


QuotationLineFormSet = inlineformset_factory(Quotation, QuotationLine, form=QuotationLineForm, extra=1)

# from django import forms
# from .models import Transaction, TransactionLine
#
#
# class PurchaseForm(forms.ModelForm):
#     class Meta:
#         model = Transaction
#         fields = ['supplier', 'date']
#         widgets = {
#             'date': forms.DateInput(attrs={'type': 'date'}),
#         }
#
#     transaction_lines = forms.inlineformset_factory(
#         Transaction,
#         TransactionLine,
#         fields=('product', 'quantity', 'price'),
#         extra=1,
#         can_delete=True,
#         widgets={
#             'product': forms.TextInput(attrs={'class': 'form-control'}),
#             'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
#             'price': forms.NumberInput(attrs={'class': 'form-control'}),
#         }
#     )
#
#
# class SaleForm(forms.ModelForm):
#     class Meta:
#         model = Transaction
#         fields = [ 'date', 'dealer']
#         widgets = {
#             'date': forms.DateInput(attrs={'type': 'date'}),
#         }
#
#
# class TransactionLineForm(forms.ModelForm):
#     class Meta:
#         model = TransactionLine
#         fields = ['product', 'quantity', 'price']
#         widgets = {
#             'product': forms.TextInput(attrs={'class': 'form-control'}),
#             'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
#             'price': forms.NumberInput(attrs={'class': 'form-control'}),
#         }
