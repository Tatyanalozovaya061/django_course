from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contacts, home, product_list

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('product/<int:pk>/', product_list, name='product_list'),
    path('contacts/', contacts, name='contacts'),
]