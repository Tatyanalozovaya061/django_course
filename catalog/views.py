from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.urls import reverse_lazy

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Category, Version
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ProductListView(LoginRequiredMixin, ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        active_versions = Version.objects.filter(is_active=True)
        if active_versions:
            context['active_versions'] = active_versions
        else:
            context['active_versions'] = None
        return context


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category


class CategoryProductListView(LoginRequiredMixin, ListView):
    model = Category

    def get_queryset(self):
        category_pk = self.kwargs['pk']
        return Product.objects.filter(category_id=category_pk)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:list')


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:list')


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)
