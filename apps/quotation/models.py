from django.conf import settings
from django.db import models


class Quotation(models.Model):
    date = models.DateTimeField()
    dealer = models.ForeignKey('partner.Dealer', on_delete=models.CASCADE)
    supplier = models.ForeignKey('partner.Supplier', on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class QuotationLine(models.Model):
    quotation = models.ForeignKey('quotation.Quotation', on_delete=models.CASCADE)
    product = models.ForeignKey('catalogue.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
