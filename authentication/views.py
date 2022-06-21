from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from .backends import UserLoginBackend
from django.contrib.auth import login as auth_login
from .decorators import unauthenticated


@unauthenticated(url='main_page')
def login(request):
    msg = ''
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = UserLoginBackend().authenticate(request, email=email, password=password)
        if user:
            auth_login(request, user)
            return redirect('main_page')
        else:
            msg = '<div class="alert alert-danger" role="alert">Błędny e-mail lub hasło</div>'

    return render(request, 'authentication/login.html', {'msg':msg})


@unauthenticated(url='main_page')
def register(request):
    form = UserRegisterForm()
    msg = ''
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_page')
        else:
            msg = '<div class="alert alert-danger" role="alert">Błędne dane</div>'
    context = {'form': form,'msg':msg}

    return render(request, 'authentication/register.html', context=context)
