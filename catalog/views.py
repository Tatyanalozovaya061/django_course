from catalog.models import Product, Category
from django.views.generic import ListView, DetailView


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class CategoryListView(ListView):
    model = Category


class CategoryProductListView(ListView):
    model = Category

    def get_queryset(self):
        category_pk = self.kwargs['pk']
        return Product.objects.filter(category_id=category_pk)
