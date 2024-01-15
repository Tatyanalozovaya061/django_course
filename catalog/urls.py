from django.urls import path
from catalog.views import ProductListView, ProductDetailView, CategoryListView, CategoryProductListView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('product_list', ProductListView.as_view(), name='list'),
    path('product_list/<int:pk>/', CategoryProductListView.as_view(), name='product_list'),
    path('detail_list/<int:pk>/', ProductDetailView.as_view(), name='detail_list'),
    path('', CategoryListView.as_view(), name='category_list')
]