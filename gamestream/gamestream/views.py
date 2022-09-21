from django.shortcuts import  render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import NewUserForm 



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

def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("/login")
	form = NewUserForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})

def subscription(request):
    context = {}
    return render(request, 'subscription.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')