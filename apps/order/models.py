from django.conf import settings
from django.db import models
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver

class Transaction(models.Model):
    PURCHASE = 'purchase'
    SALE = 'sale'

    TRANSACTION_TYPE_CHOICES = [
        (PURCHASE, 'Purchase'),
        (SALE, 'Sale'),
    ]

    date = models.DateTimeField(default=datetime.now)
    dealer = models.ForeignKey('partner.Dealer', on_delete=models.CASCADE, null=True, blank=False)
    supplier = models.ForeignKey('partner.Supplier', on_delete=models.CASCADE, null=True, blank=False)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def price(self):
        return self.lines.all().aggregate(total=models.Sum('price'))['total'] or 0

    def __str__(self):
        return f"{self.transaction_type} at {self.created_at}"


class TransactionLine(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='lines')
    product = models.ForeignKey('catalogue.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.transaction.transaction_type == Transaction.PURCHASE:
            self.product.net_count += self.quantity
        elif self.transaction.transaction_type == Transaction.SALE:
            self.product.net_count -= self.quantity
        self.product.save()

    def __str__(self):
        return f"TransactionLine #{self.pk} - Transaction: {self.transaction.pk}, Product: {self.product.name}"

# Register a signal receiver to update the net count field when a TransactionLine is saved
@receiver(post_save, sender=TransactionLine)
def update_product_net_count(sender, instance, **kwargs):
    instance.product.save()



# from django.conf import settings
# from django.db import models
# from datetime import datetime
#
#
# class Transaction(models.Model):
#     PURCHASE = 'purchase'
#     SALE = 'sale'
#     TRANSACTION_TYPE_CHOICES = [
#         (PURCHASE, 'Purchase'),
#         (SALE, 'Sale'),
#     ]
#
#     date = models.DateTimeField(default=datetime.now)
#     dealer = models.ForeignKey('partner.Dealer', on_delete=models.CASCADE,null=True,blank=False)
#     supplier = models.ForeignKey('partner.Supplier', on_delete=models.CASCADE,null=True,blank=False)
#     transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
#     created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"{self.transaction_type} at {self.created_at}"
#
#
# class TransactionLine(models.Model):
#     transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
#     product = models.ForeignKey('catalogue.Product', on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=0)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
