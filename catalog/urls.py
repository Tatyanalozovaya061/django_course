from django.urls import path
from catalog.views import index, contacts, home

urlpatterns = [
    path('', index),
    path('contacts', contacts),
    path('home', home),
]