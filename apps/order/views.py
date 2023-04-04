from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction, TransactionLine
from apps.quotation.models import Quotation
from .forms import TransactionLineForm, SaleForm, QuotationLineFormSet
from django.db import transaction

TransactionLineFormSet = inlineformset_factory(Transaction, TransactionLine, form=TransactionLineForm, extra=1)


class PurchaseCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    fields = ['date', 'dealer']
    template_name = 'order/purchase_create.html'
    success_url = reverse_lazy('order:purchase_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = TransactionLineFormSet(self.request.POST, instance=self.object)
        else:
            data['lines'] = TransactionLineFormSet(instance=self.object)
        return data

    object = None

    def form_valid(self, form):
        context = self.get_context_data()
        lines = context['lines']
        with transaction.atomic():
            if lines.is_valid():
                form.save(commit=False)
                form.instance.transaction_type = Transaction.PURCHASE
                form.instance.created_by = self.request.user
                self.object = form.save()
                lines.instance = self.object
                lines.save()
                out = HttpResponseRedirect(self.get_success_url() + "?success=1")
            else:
                form.add_error(None, "Please correct the errors below.")
                out = self.render_to_response(context)
        return out


class PurchaseListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'order/purchase_list.html'
    context_object_name = 'transactions'
    ordering = ['-created_at']
    paginate_by = 10

    def get_queryset(self):
        return Transaction.objects.filter(transaction_type=Transaction.PURCHASE)


class PurchaseDetailView(LoginRequiredMixin, DetailView):
    model = Transaction
    template_name = 'order/purchase_detail.html'
    context_object_name = 'transaction'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        transaction = self.get_object()
        context['lines'] = TransactionLine.objects.filter(transaction=transaction)
        context['total_price'] = sum(line.price * line.quantity for line in transaction.lines.all())
        return context


class PurchaseDeleteView(LoginRequiredMixin, DeleteView):
    model = Transaction
    template_name = 'order/purchase_confirm_delete.html'
    success_url = reverse_lazy('order:purchase_list')


class PurchaseUpdateView(LoginRequiredMixin, UpdateView):
    model = Transaction
    fields = ['date', 'supplier']
    template_name = 'order/purchase_update.html'
    success_url = reverse_lazy('order:purchase_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = TransactionLineFormSet(self.request.POST, instance=self.object)
        else:
            data['lines'] = TransactionLineFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        lines = context['lines']
        with transaction.atomic():
            if lines.is_valid():
                form.save(commit=False)
                form.instance.transaction_type = Transaction.PURCHASE
                form.instance.created_by = self.request.user
                self.object = form.save()
                lines.instance = self.object
                for form in lines.forms:
                    form.save(commit=False)
                    form.transaction = self.object
                lines.save()
                out = HttpResponseRedirect(self.get_success_url())
            else:
                form.add_error(None, "Please correct the errors below.")
                out = self.render_to_response(context)
        return out



class SaleCreateView(LoginRequiredMixin, CreateView):
    model = Quotation
    form_class = SaleForm
    template_name = 'order/sale_create.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['quotationlines'] = QuotationLineFormSet(self.request.POST)
        else:
            data['quotationlines'] = QuotationLineFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        quotationlines = context['quotationlines']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if quotationlines.is_valid():
                quotationlines.instance = self.object
                quotationlines.save()
        return super().form_valid(form)


class SaleListView(LoginRequiredMixin, ListView):
    model = Quotation
    template_name = 'order/sale_list.html'
    context_object_name = 'quotations'

    def get_queryset(self):
        return super().get_queryset()


class SaleDetailView(LoginRequiredMixin, DetailView):
    model = Quotation
    template_name = 'order/sale_detail.html'
    context_object_name = 'quotation'


# from django.shortcuts import get_object_or_404
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin
# from .models import Transaction,TransactionLine
# from apps.quotation.models import QuotationLine
# from apps.catalogue.models import Product
# from .forms import PurchaseForm,SaleForm,TransactionLineForm
# from django.forms import modelformset_factory
#
#
# class PurchaseListView(LoginRequiredMixin, ListView):
#     model = Transaction
#     template_name = 'order/purchase_list.html'
#     context_object_name = 'purchases'
#     ordering = ['-created_at']
#
#
# class PurchaseDetailView(LoginRequiredMixin, DetailView):
#     model = Transaction
#     template_name = 'order/purchase_detail.html'
#     context_object_name = 'purchase'
#
# class PurchaseCreateView(LoginRequiredMixin, CreateView):
#     model = Transaction
#     template_name = 'order/purchase_create.html'
#     fields = ['date', 'supplier']
#     success_url = reverse_lazy('order:purchase_list')
#
#     def get_context_data(self, **kwargs):
#         data = super(PurchaseCreateView, self).get_context_data(**kwargs)
#         if self.request.POST:
#             data['lines'] = TransactionLineFormSet(self.request.POST)
#         else:
#             data['lines'] = TransactionLineFormSet()
#         return data
#
#     def form_valid(self, form):
#         context = self.get_context_data()
#         lines = context['lines']
#         with transaction.atomic():
#             self.object = form.save(commit=False)
#             self.object.created_by = self.request.user
#             self.object.save()
#             if lines.is_valid():
#                 lines.instance = self.object
#                 lines.save()
#         return super().form_valid(form)
#
# class PurchaseUpdateView(LoginRequiredMixin, UpdateView):
#     model = Transaction
#     template_name = 'order/purchase_update.html'
#     fields = ['date', 'supplier', 'total_amount']
#     success_url = reverse_lazy('order:purchase_list')
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)
#
#
# class PurchaseDeleteView(LoginRequiredMixin, DeleteView):
#     model = Transaction
#     template_name = 'order/purchase_confirm_delete.html'
#     success_url = reverse_lazy('order:purchase_list')
#
#
#
# class SaleListView(LoginRequiredMixin, ListView):
#     model = Transaction
#     queryset = Transaction.objects.filter(transaction_type='sale')
#     template_name = 'order/sale_list.html'
#     context_object_name = 'sales'
#     ordering = ['-created_at']
#
#
# class SaleDetailView(LoginRequiredMixin, DetailView):
#     model = Transaction
#     queryset = Transaction.objects.filter(transaction_type='sale')
#     template_name = 'order/sale_detail.html'
#     context_object_name = 'sale'
#
#
# class SaleCreateView(LoginRequiredMixin, CreateView):
#     model = Transaction
#     template_name = 'order/sale_create.html'
#     form_class = SaleForm
#     initial = {'transaction_type': 'sale'}
#     success_url = reverse_lazy('order:sale_list')
#
#     def form_valid(self, form):
#         quotation_line = get_object_or_404(QuotationLine, pk=self.kwargs['quotation_line_id'])
#         if quotation_line.status == 'accepted':
#             form.instance.created_by = self.request.user
#             form.instance.customer = quotation_line.quotation.customer
#             response = super().form_valid(form)
#
#             # create transaction line based on quotation line
#             TransactionLine.objects.create(sale=form.instance, product=quotation_line.product,
#                                      quantity=quotation_line.quantity, price=quotation_line.price,
#                                      created_by=self.request.user)
#             form.instance.total_amount = self.object.transactionline_set.aggregate(total=models.Sum('price'))['total']
#             form.save()
#             return super().form_valid(form)
#         else:
#             return super().form_invalid(form)
#
#
#
# class SaleUpdateView(LoginRequiredMixin, UpdateView):
#     model = Transaction
#     fields = ['date', 'dealer','created_by']
#     template_name = 'order/sale_form.html'
#     queryset = Transaction.objects.filter(transaction_type='sale')
#     success_url = reverse_lazy('order:sale_list')
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)
#
#
# class SaleDeleteView(LoginRequiredMixin, DeleteView):
#     model = Transaction
#     queryset = Transaction.objects.filter(transaction_type='sale')
#     template_name = 'order/sale_confirm_delete.html'
#     success_url = reverse_lazy('order:sale_list')



# from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
# from django.urls import reverse_lazy
# from .models import Transaction, TransactionLine
#
# class TransactionCreateView(CreateView):
#     model = Transaction
#     fields = ['date', 'dealer', 'supplier', 'transaction_type']
#     template_name = 'order/purchase_create.html'
#     success_url = reverse_lazy('order:transaction_list')
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)
#
# class TransactionUpdateView(UpdateView):
#     model = Transaction
#     fields = ['date', 'dealer', 'supplier', 'transaction_type']
#     template_name = 'order/purchase_create.html'
#     success_url = reverse_lazy('order:transaction_list')
#
# class TransactionDetailView(DetailView):
#     model = Transaction
#     template_name = 'order/purchase_detail.html'
#
# class TransactionDeleteView(DeleteView):
#     model = Transaction
#     template_name = 'order/base.html'
#     success_url = reverse_lazy('order:transaction_list')
#
# class TransactionListView(ListView):
#     model = Transaction
#     template_name = 'order/purchase_list.html'
#     paginate_by = 10
#
# class TransactionLineCreateView(CreateView):
#     model = TransactionLine
#     fields = ['transaction', 'product', 'quantity', 'price']
#     template_name = 'order/purchase_confirm_delete.html'
#     success_url = reverse_lazy('order:transaction_list')
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)
#
# class TransactionLineUpdateView(UpdateView):
#     model = TransactionLine
#     fields = ['transaction', 'product', 'quantity', 'price']
#     template_name = 'order/purchase_confirm_delete.html'
#     success_url = reverse_lazy('order:transaction_list')
#
# class TransactionLineDetailView(DetailView):
#     model = TransactionLine
#     template_name = 'order/purchase_form.html'
#
# class TransactionLineDeleteView(DeleteView):
#     model = TransactionLine
#     template_name = 'order/sale_form.html'
#     success_url = reverse_lazy('order:transaction_list')
#
# class TransactionLineListView(ListView):
#     model = TransactionLine
#     template_name = 'order/sale_list.html'
#     paginate_by = 10
#


# from django.urls import reverse_lazy
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from .models import Transaction, TransactionLine
#
# class TransactionListView(ListView):
#     model = Transaction
#     template_name = 'purchase_list.html'
#
# class TransactionDetailView(DetailView):
#     model = Transaction
#     template_name = 'purchase_detail.html'
#
# class TransactionCreateView(CreateView):
#     model = Transaction
#     fields = ['dealer', 'supplier', 'transaction_type']
#     template_name = 'purchase_create.html'
#     success_url = reverse_lazy('transaction_list')
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)
#
# class TransactionUpdateView(UpdateView):
#     model = Transaction
#     fields = ['dealer', 'supplier', 'transaction_type']
#     template_name = 'purchase_create.html'
#     success_url = reverse_lazy('transaction_list')
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)
#
# class TransactionDeleteView(DeleteView):
#     model = Transaction
#     template_name = 'base.html'
#     success_url = reverse_lazy('transaction_list')
#
# class TransactionLineCreateView(CreateView):
#     model = TransactionLine
#     fields = ['transaction', 'product', 'quantity', 'price']
#     template_name = 'purchase_confirm_delete.html'
#
#     def get_success_url(self):
#         return reverse_lazy('transaction_detail', kwargs={'pk': self.object.transaction.pk})
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)
#
# class TransactionLineUpdateView(UpdateView):
#     model = TransactionLine
#     fields = ['transaction', 'product', 'quantity', 'price']
#     template_name = 'purchase_confirm_delete.html'
#
#     def get_success_url(self):
#         return reverse_lazy('transaction_detail', kwargs={'pk': self.object.transaction.pk})
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)
#
# class TransactionLineDeleteView(DeleteView):
#     model = TransactionLine
#     template_name = 'sale_form.html'
#
#     def get_success_url(self):
#         return reverse_lazy('transaction_detail', kwargs={'pk': self.object.transaction.pk})


# from django.shortcuts import render, redirect
# from .models import Transaction, TransactionLine
#
# def create_purchase(request):
#     if request.method == 'POST':
#         # Handle form submission and create a new Transaction object
#         # with the purchase transaction type
#         dealer = request.POST['dealer']
#         supplier = request.POST['supplier']
#         created_by = request.user
#         transaction = Transaction.objects.create(
#             dealer=dealer,
#             supplier=supplier,
#             transaction_type=Transaction.PURCHASE,
#             created_by=created_by
#         )
#         # Loop over the form data for each transaction line and create a new
#         # TransactionLine object for each one
#         for i in range(1, 6):
#             product_id = request.POST.get(f'product_{i}')
#             quantity = request.POST.get(f'quantity_{i}')
#             price = request.POST.get(f'price_{i}')
#             if product_id and quantity and price:
#                 product = Product.objects.get(id=product_id)
#                 TransactionLine.objects.create(
#                     transaction=transaction,
#                     product=product,
#                     quantity=quantity,
#                     price=price,
#                     created_by=created_by
#                 )
#         return redirect('dashboard')
#     else:
#         # Render the purchase form template
#         return render(request, 'purchase.html')
#
# def create_sale(request):
#     if request.method == 'POST':
#         # Handle form submission and create a new Transaction object
#         # with the sale transaction type
#         dealer = request.POST['dealer']
#         supplier = request.POST['supplier']
#         created_by = request.user
#         transaction = Transaction.objects.create(
#             dealer=dealer,
#             supplier=supplier,
#             transaction_type=Transaction.SALE,
#             created_by=created_by
#         )
#         # Get the quotation and loop over each line to create a new
#         # TransactionLine object for each one
#         quotation_id = request.POST['quotation_id']
#         quotation = Quotation.objects.get(id=quotation_id)
#         for line in quotation.lines.all():
#             TransactionLine.objects.create(
#                 transaction=transaction,
#                 product=line.product,
#                 quantity=line.quantity,
#                 price=line.price,
#                 created_by=created_by
#             )
#         return redirect('dashboard')
#     else:
#         # Render the sale form template with a dropdown to select the quotation
#         quotations = Quotation.objects.all()
#         return render(request, 'sale.html', {'quotations': quotations})


# from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView ,UpdateView
# from .models import Purchase,Sale, TransactionLine
#
# class PurchaseCreateView(CreateView):
#     model = Purchase
#     fields = ['dealer', 'supplier']
#     template_name = 'purchase_form.html'
#     success_url = reverse_lazy('purchase_list')
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         response = super().form_valid(form)
#         # Create a new transaction line for each product in the purchase
#         products = self.request.POST.getlist('product')
#         quantities = self.request.POST.getlist('quantity')
#         prices = self.request.POST.getlist('price')
#         for i in range(len(products)):
#             TransactionLine.objects.create(
#                 transaction=self.object,
#                 product_id=products[i],
#                 quantity=quantities[i],
#                 price=prices[i],
#                 created_by=self.request.user
#             )
#         return response
#
# class SaleUpdateView(UpdateView):
#     model = Sale
#     fields = ['quotation_number']
#     template_name = 'sale_form.html'
#     success_url = reverse_lazy('sale_list')
#
#     def form_valid(self, form):
#         response = super().form_valid(form)
#         # Update the transaction lines with the new quotation number
#         for line in self.object.lines.all():
#             line.product.quotation_number = form.cleaned_data['quotation_number']
#             line.product.save()
#         return response
#


# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Sale, Purchase, TransactionLine
# from .forms import TransactionForm, TransactionLineForm
#
#
# class SaleListView(ListView):
#     model = Sale
#     template_name = 'order/sale_list.html'
#     context_object_name = 'sales'
#     ordering = ['-created_at']
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         queryset = queryset.filter(created_by=self.request.user)
#         return queryset
#
# class SaleDetailView(DetailView):
#     model = Sale
#     template_name = 'order/sale_detail.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['lines'] = self.object.lines.all()
#         return context
#
#
# class SaleCreateView(CreateView):
#     model = Sale
#     template_name = 'order/sale_create.html'
#     fields = ['product', 'quantity', 'price']
#     success_url = reverse_lazy('order:sale_list')
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         form.save()
#         return super().form_valid(form)
#
#
# class SaleUpdateView(UpdateView):
#     model = Sale
#     form_class = TransactionForm
#     template_name = 'order/purchase_update.html'
#     success_url = reverse_lazy('order:sale_list')
#
#
# class SaleDeleteView(DeleteView):
#     model = Sale
#     template_name = 'order/sale_delete.html'
#     success_url = reverse_lazy('order:sale_list')
#
#
# class PurchaseListView(ListView):
#     model = Purchase
#     template_name = 'order/purchase_list.html'
#
#
# class PurchaseDetailView(DetailView):
#     model = Purchase
#     template_name = 'order/purchase_detail.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['lines'] = self.object.lines.all()
#         return context
#
#
# class PurchaseCreateView(CreateView):
#     model = Purchase
#     form_class = TransactionForm
#     template_name = 'order/purchase_create.html'
#     success_url = reverse_lazy('order:purchase_list')
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         response = super().form_valid(form)
#         return response
#
#
# class PurchaseUpdateView(UpdateView):
#     model = Purchase
#     form_class = TransactionForm
#     template_name = 'order/purchase_update.html'
#     success_url = reverse_lazy('order:purchase_list')
#
#
# class PurchaseDeleteView(DeleteView):
#     model = Purchase
#     template_name = 'order/purchase_delete.html'
#     success_url = reverse_lazy('order:purchase_list')
#
#
# class TransactionLineCreateView(CreateView):
#     model = TransactionLine
#     form_class = TransactionLineForm
#     template_name = 'order/base.html'
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         response = super().form_valid(form)
#         return response
#
#
# @receiver(post_save, sender=Sale)
# def create_sale_line(sender, instance, created, **kwargs):
#     if created:
#         for line in instance.lines.all():
#             TransactionLine.objects.create(
#                 transaction=instance,
#                 product=line.product,
#                 quantity=line.quantity,
#                 price=line.price,
#                 created_by=instance.created_by,
#             )
#
#
# @receiver(post_save, sender=Purchase)
# def create_purchase_line(sender, instance, created, **kwargs):
#     if created:
#         for line in instance.lines.all():
#             TransactionLine.objects.create(
#                 transaction=instance,
#                 product=line.product,
#                 quantity=line.quantity,
#                 price=line.price,
#                 created_by=instance.created_by,
#             )


#     from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
#
# from django.urls import reverse_lazy
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Transaction, TransactionLine
# from catalogue.models import Product
#
# class TransactionListView(ListView):
#     model = Transaction
#     template_name = 'sale_list.html'
#     context_object_name = 'transactions'
#     ordering = ['-created_at']
#
# class TransactionCreateView(CreateView):
#     model = Transaction
#     template_name = 'transaction_confirm_delete'
#     fields = '__all__'
#     success_url = reverse_lazy('transaction_list')
#
# class TransactionDetailView(DetailView):
#     model = Transaction
#     template_name = 'sale_detail.html'
#     context_object_name = 'transaction'
#
# class TransactionUpdateView(UpdateView):
#     model = Transaction
#     template_name = 'transaction_confirm_delete'
#     fields = '__all__'
#     success_url = reverse_lazy('transaction_list')
#
# class TransactionDeleteView(DeleteView):
#     model = Transaction
#     template_name = 'base.html'
#     success_url = reverse_lazy('transaction_list')
#
# @receiver(post_save, sender=TransactionLine)
# def update_product_quantity(sender, instance, **kwargs):
#     product = instance.product
#     quantity = instance.quantity
#     if instance.transaction.transaction_type == 'sale':
#         quantity


# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin
# from .models import Transaction
#
# class TransactionListView(LoginRequiredMixin, ListView):
#     model = Transaction
#     template_name = 'order/sale_list.html'
#     context_object_name = 'transactions'
#     paginate_by = 10
#
# class TransactionDetailView(LoginRequiredMixin, DetailView):
#     model = Transaction
#     template_name = 'order/sale_detail.html'
#
# class TransactionCreateView(LoginRequiredMixin, CreateView):
#     model = Transaction
#     template_name = 'order/transaction_confirm_delete'
#     fields = ['transaction_type', 'dealer', 'supplier', 'product', 'quantity', 'price']
#     success_url = reverse_lazy('order:transaction_list')
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)
#
# class TransactionUpdateView(LoginRequiredMixin, UpdateView):
#     model = Transaction
#     template_name = 'order/purchase_update.html'
#     fields = ['transaction_type', 'dealer', 'supplier', 'product', 'quantity', 'price']
#     success_url = reverse_lazy('order:transaction_list')
#
# class TransactionDeleteView(LoginRequiredMixin, DeleteView):
#     model = Transaction
#     template_name = 'order/sale_delete.html'
#     success_url = reverse_lazy('order:transaction_list')


# from django.shortcuts import render, get_object_or_404
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin
# from .models import Transaction, TransactionLine
#
#
#
# class TransactionListView(LoginRequiredMixin, ListView):
#     model = Transaction
#     template_name = 'order/sale_list.html'
#     context_object_name = 'transaction'
#     ordering = ['-created_at']
#
#
# class TransactionDetailView(LoginRequiredMixin, DetailView):
#     model = Transaction
#     template_name = 'order/sale_detail.html'
#     context_object_name = 'transaction'
#
#
# class TransactionCreateView(LoginRequiredMixin, CreateView):
#     model = Transaction
#     template_name = 'order/transaction_confirm_delete'
#     fields = ['date', 'dealer', 'supplier', 'transaction_type']
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)
#
#
# class TransactionUpdateView(LoginRequiredMixin, UpdateView):
#     model = Transaction
#     template_name = 'order/transaction_confirm_delete'
#     fields = ['date', 'dealer', 'supplier', 'transaction_type']
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)
#
#
# class TransactionDeleteView(LoginRequiredMixin, DeleteView):
#     model = Transaction
#     template_name = 'order/sale_delete.html'
#     success_url = reverse_lazy('order:transaction_list')
#
#
# class TransactionLineCreateView(LoginRequiredMixin, CreateView):
#     model = TransactionLine
#     template_name = 'order/purchase_confirm_delete.html'
#     fields = ['transaction', 'product', 'quantity', 'price']
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)
#
#
# class TransactionLineUpdateView(LoginRequiredMixin, UpdateView):
#     model = TransactionLine
#     template_name = 'order/purchase_confirm_delete.html'
#     fields = ['transaction', 'product', 'quantity', 'price']
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)
#
#
# class TransactionLineDeleteView(LoginRequiredMixin, DeleteView):
#     model = TransactionLine
#     template_name = 'order/transactionline_delete.html'
#     success_url = reverse_lazy('order:transaction_list')
#


# from django.shortcuts import render, get_object_or_404, redirect
# from django.views.generic import ListView, CreateView, DetailView
# from django.urls import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.messages.views import SuccessMessageMixin
# from django.contrib import messages
# from .models import Transaction, TransactionLine
#
# class TransactionListView(LoginRequiredMixin, ListView):
#     model = Transaction
#     template_name = 'order/sale_list.html'
#     context_object_name = 'transactions'
#     ordering = ['-created_at']
#     paginate_by = 10
#
# class TransactionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
#     model = Transaction
#     template_name = 'order/transaction_confirm_delete'
#     fields = ['date', 'dealer', 'supplier', 'transaction_type']
#     success_message = 'Transaction was created successfully!'
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)
#
# class TransactionDetailView(LoginRequiredMixin, DetailView):
#     model = Transaction
#     template_name = 'order/sale_detail.html'
#     context_object_name = 'transaction'
#
# class TransactionLineCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
#     model = TransactionLine
#     template_name = 'order/purchase_confirm_delete.html'
#     fields = ['product', 'quantity', 'price']
#     success_message = 'Transaction line was created successfully!'
#
#     def form_valid(self, form):
#         form.instance.transaction_id = self.kwargs['pk']
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse_lazy('order:transaction_detail', kwargs={'pk': self.kwargs['pk']})
#
# def transaction_delete(request, pk):
#     transaction = get_object_or_404(Transaction, pk=pk)
#     if request.method == 'POST':
#         transaction.delete()
#         messages.success(request, 'Transaction was deleted successfully!')
#         return redirect('transaction_list')
#     return render(request, 'sale_delete.html', {'transaction': transaction})
#
# def transaction_line_delete(request, pk):
#     transaction_line = get_object_or_404(TransactionLine, pk=pk)
#     transaction_pk = transaction_line.transaction.pk
#     if request.method == 'POST':
#         transaction_line.delete()
#         messages.success(request, 'Transaction line was deleted successfully!')
#         return redirect('transaction_detail', pk=transaction_pk)
#     return render(request, 'transactionline_delete.html', {'transaction_line': transaction_line})
