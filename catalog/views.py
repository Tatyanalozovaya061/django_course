from django.shortcuts import render, redirect
from catalog.models import Category, Product


def index(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Магазин продуктов - главная'
    }
    return render(request, 'catalog/index.html', context)


def product_list(request, pk):
    context = {
        'object': Product.objects.get(id=pk),
    }
    return render(request, 'catalog/product_list.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        if name is not None and email is not None:
            return render(request, 'catalog/contacts.html', context={'name': name, 'email': email})
    return render(request, 'catalog/contacts.html')

def home(request):
    return render(request, 'catalog/home.html')
