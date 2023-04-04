from django import forms
from django.forms import inlineformset_factory

from .models import Quotation, QuotationLine


class QuotationForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = ('dealer', 'district')


class QuotationLineForm(forms.ModelForm):
    class Meta:
        model = QuotationLine
        fields = ('product', 'quantity', 'price')



QuotationLineFormSet = inlineformset_factory(
    Quotation, QuotationLine, form=QuotationLineForm,
    extra=1, can_delete=False
)
