from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from .backends import UserLoginBackend
from django.contrib.auth import login as auth_login
from .decorators import unauthenticated


@unauthenticated(url='home')
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = UserLoginBackend().authenticate(request, email=email, password=password)
        if user:
            auth_login(request, user)
            return redirect('home')

    return render(request, 'authentication/login.html', {})


@unauthenticated(url='home')
def register(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')

    context = {'form': form}

    return render(request, 'authentication/register.html', context=context)
