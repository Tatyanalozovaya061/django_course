from django.shortcuts import render

def index(request):
    return render(request, 'catalog/index.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        if name is not None and email is not None:
            return render(request, 'catalog/contacts.html', context={'name': name, 'email': email})
    return render(request, 'catalog/contacts.html')

def home(request):
    return render(request, 'catalog/home.html')
