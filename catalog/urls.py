from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import (ProductListView, ProductDetailView, CategoryListView, CategoryProductListView,
                           ProductCreateView, ProductUpdateView, ProductDeleteView, VersionCreateView)
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('product_list', ProductListView.as_view(), name='list'),
    path('product_list/<int:pk>/', CategoryProductListView.as_view(), name='product_list'),
    path('detail_list/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='detail_list'),
    path('', CategoryListView.as_view(), name='category_list'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('versions/create/', VersionCreateView.as_view(), name='create_version'),
]
