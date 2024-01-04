from django.shortcuts import render, redirect
from catalog.models import Category, Product


def index(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Магазин продуктов'
    }
    return render(request, 'catalog/index.html', context)

def product(request, pk):
    context = {
        'object_list': Product.objects.filter(id=pk)
    }
    return render(request, 'catalog/product.html', context)

def product_list(request):
    if request.method == 'POST':
        # Обработка нажатия кнопки
        # Вы можете выполнить здесь необходимые действия или перенаправить пользователя на другую страницу
        return redirect('новая_страница')
    else:
        return render(request, 'product_list.html')

# def categories(request):
#     context = {
#         'object_list': Category.objects.all(),
#         'title': 'Магазин продуктов'
#     }
#     return render(request, 'catalog/index.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        if name is not None and email is not None:
            return render(request, 'catalog/contacts.html', context={'name': name, 'email': email})
    return render(request, 'catalog/contacts.html')

def home(request):
    return render(request, 'catalog/home.html')
