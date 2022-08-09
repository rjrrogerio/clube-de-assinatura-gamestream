from django.shortcuts import render


# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def cart(request):
    context = {}
    return render(request, 'cart.html', context)

def login(request):
    context = {}
    return render(request, 'login.html', context)

def register(request):
    context = {}
    return render(request, 'register.html', context)