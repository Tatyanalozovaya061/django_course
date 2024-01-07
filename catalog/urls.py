from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contacts, home, product

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/product_list', product, name='product_list'),
    path('product/', product, name='product'),
    path('contacts/', contacts, name='contacts'),
]