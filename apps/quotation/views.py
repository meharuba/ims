from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Quotation, QuotationLine
from .forms import QuotationForm, QuotationLineFormSet
from django.db import transaction
from django.urls import reverse_lazy


class QuotationList(ListView):
    model = Quotation
    template_name = 'quotation_list.html'
    ordering = ('-id', )




class QuotationDetail(DetailView):
    model = Quotation
    template_name = 'quotation_detail.html'
    context_object_name = 'quotation'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quotation = self.get_object()
        context['total_price'] = sum(line.price * line.quantity for line in quotation.quotationline_set.all())
        return context



# class QuotationLineDetail(DetailView):
#     model = QuotationLine
#     template_name = "quotation_detail.html"
#

class QuotationCreate(CreateView):
    model = Quotation
    form_class = QuotationForm
    template_name = 'quotation_form.html'
    success_url = reverse_lazy('quotation:quotation_list')

    def get_context_data(self, **kwargs):
        data = super(QuotationCreate, self).get_context_data(**kwargs)

        if self.request.POST:
            data['lines'] = QuotationLineFormSet(self.request.POST)
        else:
            data['lines'] = QuotationLineFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        lines = context['lines']
        with transaction.atomic():
            if lines.is_valid():
                self.object = form.save(commit=False)
                self.object.created_by = self.request.user
                self.object.save()
                lines.instance = self.object
                lines.save()
            else:
                return self.render_to_response(context)
        return super().form_valid(form)


class QuotationUpdate(UpdateView):
    model = Quotation
    form_class = QuotationForm
    template_name = 'quotation_form.html'
    success_url = reverse_lazy('quotation:quotation_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lines'] = QuotationLineFormSet(self.request.POST, instance=self.object)
        else:
            data['lines'] = QuotationLineFormSet(instance=self.object, queryset=self.object.quotationline_set.all())
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        lines = context['lines']
        with transaction.atomic():
            self.object = form.save()
            if lines.is_valid():
                lines.instance = self.object
                lines.save()
        return super().form_valid(form)


class QuotationDelete(DeleteView):
    model = Quotation
    template_name = 'quotation_confirm_delete.html'
    success_url = reverse_lazy('quotation:quotation_list')

# from django.shortcuts import render, get_object_or_404
# from .models import Quotation
# from .forms import QuotationForm
#
# def QuotationDetail(request, pk):
#     quotation = get_object_or_404(Quotation, pk=pk)
#     form = QuotationForm(instance=quotation)
#     context = {'quotation': quotation, 'form': form}
#     return render(request, 'quotation/detail.html', context)
