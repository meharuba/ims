from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product, Category
from .forms import ProductForm, CategoryForm
from django.utils import timezone



class ProductListView(ListView):
    model = Product
    template_name = 'catalogue/product_list.html'
    context_object_name = 'products'

class CategoryListView(ListView):
    model = Category
    template_name = 'catalogue/category_list.html'
    context_object_name = 'categories'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalogue/product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'pk'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'catalogue/category_detail.html'
    context_object_name = 'category'
    pk_url_kwarg = 'pk'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalogue/product_create.html'
    success_url = reverse_lazy('catalogue:product_list')

    def form_valid(self, form):
        product = form.save(commit=False)
        if self.request.user.is_authenticated:
            product.created_by_id = self.request.user.pk
            product.created_at = timezone.now()
        product.save()
        return super().form_valid(form)

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalogue/category_create.html'
    success_url = reverse_lazy('catalogue:category_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalogue/product_update.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('catalogue:product_list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalogue/category_update.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('catalogue:category_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalogue/product_delete.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('catalogue:product_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'catalogue/category_delete.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('catalogue:category_list')








