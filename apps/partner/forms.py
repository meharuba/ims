from django import forms
from .models import District, Dealer, Supplier

class DistrictForm(forms.ModelForm):
    class Meta:
        model = District
        fields = ('name',)

class DealerForm(forms.ModelForm):
    class Meta:
        model = Dealer
        fields = ('name', 'email', 'phone', 'district')

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ('name', 'email', 'phone', 'district')
