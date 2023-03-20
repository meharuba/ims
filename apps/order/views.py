from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction, TransactionLine



class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'order/transaction_list.html'
    context_object_name = 'transaction'
    ordering = ['-created_at']


class TransactionDetailView(LoginRequiredMixin, DetailView):
    model = Transaction
    template_name = 'order/transaction_detail.html'
    context_object_name = 'transaction'


class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    template_name = 'order/transaction_form.html'
    fields = ['date', 'dealer', 'supplier', 'transaction_type']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    model = Transaction
    template_name = 'order/transaction_form.html'
    fields = ['date', 'dealer', 'supplier', 'transaction_type']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    model = Transaction
    template_name = 'order/transaction_delete.html'
    success_url = reverse_lazy('order:transaction-list')


class TransactionLineCreateView(LoginRequiredMixin, CreateView):
    model = TransactionLine
    template_name = 'order/transactionline_form.html'
    fields = ['transaction', 'product', 'quantity', 'price']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TransactionLineUpdateView(LoginRequiredMixin, UpdateView):
    model = TransactionLine
    template_name = 'order/transactionline_form.html'
    fields = ['transaction', 'product', 'quantity', 'price']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TransactionLineDeleteView(LoginRequiredMixin, DeleteView):
    model = TransactionLine
    template_name = 'order/transactionline_delete.html'
    success_url = reverse_lazy('order:transaction_list')


