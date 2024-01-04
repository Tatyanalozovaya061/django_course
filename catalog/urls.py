from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contacts, home, product

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    #path('product/', product, name='product'),
    path('product/<int:pk>/', product, name='product'),
    path('contacts/', contacts),
    #path('home/', home),
    #path('categories/',categories, name='categories')
]