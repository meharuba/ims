from .forms import DistrictForm, DealerForm, SupplierForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import District
from .models import Dealer
from .models import Supplier
from django.contrib.auth.decorators import login_required
from .forms import SupplierForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import DistrictForm



@login_required
def admin_supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            supplier = form.save(commit=False)
            supplier.created_by = request.user
            supplier.save()
            return redirect('supplier_list')
    else:
        form = SupplierForm()
    return render(request, 'create_supplier.html', {'form': form})

@login_required
def admin_district_create(request):
    if request.method == 'POST':
        form = DistrictForm(request.POST)
        if form.is_valid():
            district = form.save(commit=False)
            district.created_by = request.user
            district.save()
            return redirect('district_list')
    else:
        form = DistrictForm()
    return render(request, 'create_district.html', {'form': form})


@login_required
def admin_dealer_create(request):
    if request.method == 'POST':
        form = DealerForm(request.POST)
        if form.is_valid():
            dealer = form.save(commit=False)
            dealer.created_by = request.user
            dealer.save()
            return redirect('dealer_list')
    else:
        form = DealerForm()
    return render(request, 'create_dealer.html', {'form': form})

def district_list(request):
    districts = District.objects.all()
    return render(request, 'district_list.html', {'districts': districts})

def dealer_list(request):
    dealers = Dealer.objects.all()
    return render(request, 'dealer_list.html', {'dealers': dealers})

def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'supplier_list.html', {'suppliers': suppliers})



def delete_district(request, district_id):
    district = District.objects.get(id=district_id)
    district.delete()
    messages.success(request, 'District has been deleted.')
    return redirect(reverse('district_list'))

def delete_dealer(request, dealer_id):
    dealer = Dealer.objects.get(id=dealer_id)
    dealer.delete()
    messages.success(request, 'Dealer has been deleted.')
    return redirect(reverse('dealer_list'))

def delete_supplier(request, supplier_id):
    supplier = Supplier.objects.get(id=supplier_id)
    supplier.delete()
    messages.success(request, 'supplier has been deleted.')
    return redirect(reverse('supplier_list'))

@login_required
def district_update(request, pk):
    district = get_object_or_404(District, pk=pk)
    if request.method == 'POST':
        form = DistrictForm(request.POST, instance=district)
        if form.is_valid():
            district = form.save(commit=False)
            district.updated_by = request.user
            district.save()
            return redirect('district_list')
    else:
        form = DistrictForm(instance=district)
    return render(request, 'edit_district.html', {'form': form, 'district': district})


def edit_dealer(request, dealer_id):
    dealer = get_object_or_404(Dealer, id=dealer_id)
    if request.method == 'POST':
        form = DealerForm(request.POST, instance=dealer)
        if form.is_valid():
            form.save()
            return redirect('dealer_list')
    else:
        form = DealerForm(instance=dealer)

    context = {
        'form': form
    }
    return render(request, 'edit_dealer.html', context)




def edit_supplier(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    form = SupplierForm(request.POST or None, instance=supplier)
    if form.is_valid():
        form.save()
        return redirect('supplier_list')
    return render(request, 'edit_supplier.html', {'form': form})




def edit_district(request, pk):
    district = get_object_or_404(District, pk=pk)
    form = DistrictForm(request.POST or None, instance=district)
    if form.is_valid():
        form.save()
        return redirect('district_list')
    return render(request, 'edit_district.html', {'form': form})



# from django.shortcuts import render, redirect, get_object_or_404
# from django.urls import reverse_lazy
# from django.contrib import messages
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic import CreateView, UpdateView, DeleteView, ListView
# from .models import District, Dealer, Supplier
# from .forms import DistrictForm, DealerForm, SupplierForm
#
#
# class DistrictListView(ListView):
#     model = District
#     template_name = 'district_list.html'
#     context_object_name = 'districts'
#
#
# class DistrictCreateView(LoginRequiredMixin, CreateView):
#     model = District
#     form_class = DistrictForm
#     template_name = 'create_district.html'
#     success_url = reverse_lazy('district_list')
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)
#
#
# class DistrictUpdateView(LoginRequiredMixin, UpdateView):
#     model = District
#     form_class = DistrictForm
#     template_name = 'edit_district.html'
#     success_url = reverse_lazy('district_list')
#
#     def form_valid(self, form):
#         form.instance.updated_by = self.request.user
#         return super().form_valid(form)
#
#
# class DistrictDeleteView(LoginRequiredMixin, DeleteView):
#     model = District
#     success_url = reverse_lazy('district_list')
#
#     def delete(self, request, *args, **kwargs):
#         messages.success(request, 'District has been deleted.')
#         return super().delete(request, *args, **kwargs)
#
#
# class DealerListView(ListView):
#     model = Dealer
#     template_name = 'dealer_list.html'
#     context_object_name = 'dealers'
#
#
# class DealerCreateView(LoginRequiredMixin, CreateView):
#     model = Dealer
#     form_class = DealerForm
#     template_name = 'create_dealer.html'
#     success_url = reverse_lazy('dealer_list')
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)
#
#
# class DealerUpdateView(LoginRequiredMixin, UpdateView):
#     model = Dealer
#     form_class = DealerForm
#     template_name = 'edit_dealer.html'
#     success_url = reverse_lazy('dealer_list')
#
#
# class DealerDeleteView(LoginRequiredMixin, DeleteView):
#     model = Dealer
#     success_url = reverse_lazy('dealer_list')
#
#     def delete(self, request, *args, **kwargs):
#         messages.success(request, 'Dealer has been deleted.')
#         return super().delete(request, *args, **kwargs)
#
#
# class SupplierListView(ListView):
#     model = Supplier
#     template_name = 'supplier_list.html'
#     context_object_name = 'suppliers'
#
#
# class SupplierCreateView(LoginRequiredMixin, CreateView):
#     model = Supplier
#     form_class = SupplierForm
#     template_name = 'create_supplier.html'
#     success_url = reverse_lazy('supplier_list')
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)
#
#
# class SupplierUpdateView(LoginRequiredMixin, UpdateView):
#     model = Supplier
#     form_class = SupplierForm
#     template_name = 'edit_supplier.html'
#     success_url = reverse_lazy('supplier_list')
#
#
# class SupplierDeleteView(LoginRequiredMixin, DeleteView):
#     model = Supplier
#     success_url = reverse_lazy('supplier_list')
#
#     def delete(self, request, *args, **kwargs):
#         messages.success(request, 'Supplier has been deleted.')
#         return super().delete(request, *args, **kwargs)
