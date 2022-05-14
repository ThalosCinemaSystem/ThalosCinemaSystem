from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

def main_page(request):
    context = {}

    return render(request, 'website/main.html', context=context)


def marathons(request):
    context = {}

    return render(request, 'website/marathons.html', context=context)


def schools(request):
    context = {}

    return render(request, 'website/schools.html', context=context)


def account(request):
    context = {}

    return render(request, 'website/account.html', context=context)


def events_and_promotions(request):
    context = {}

    return render(request, 'website/events_and_promotions.html', context=context)


def repertoire(request):
    context = {}

    return render(request, 'website/repertoire.html', context=context)


def error_404(request, exception):
    data = {"error_http": "Błąd 404"}
    return render(request, 'website/error_http.html', context=data)


def error_500(request):
    data = {"error_http": "Błąd 500"}
    return render(request, 'website/error_http.html', context=data)

def logoutUser(request):
    logout(request)
    return redirect(main_page)

def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                return redirect('change_password')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'website/change_password.html', {
            'form': form
        })
    else:
        return redirect(main_page)