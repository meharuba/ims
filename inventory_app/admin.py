from django.contrib import admin
from .models import District, Dealer, Supplier, Category, Product, Transaction, TransactionLine, Quotation, QuotationLine

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    pass

@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    pass

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass

@admin.register(TransactionLine)
class TransactionLineAdmin(admin.ModelAdmin):
    pass

@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    pass

@admin.register(QuotationLine)
class QuotationLineAdmin(admin.ModelAdmin):
    pass
