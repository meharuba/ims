from django.conf import settings
from django.db import models


class Quotation(models.Model):
    dealer = models.ForeignKey('partner.Dealer', on_delete=models.CASCADE)
    district = models.ForeignKey('partner.District', on_delete=models.CASCADE, default=0)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def price(self):
        return self.quotationline_set.all().aggregate(total=models.Sum('price'))['total'] or 0

    # @property
    # def price(self):
    #     return sum(line.price for line in self.quotationline_set.all())

    def __str__(self):
        return f"Quotation #{self.pk} - Dealer: {self.dealer.name}, District: {self.district.name}"


class QuotationLine(models.Model):
    quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey('catalogue.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"QuotationLine #{self.pk} - Quotation: {self.quotation.pk}, Product: {self.product.name}"


