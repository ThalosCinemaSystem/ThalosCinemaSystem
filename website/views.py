from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    context = {}

    return render(request, 'website/main.html', context=context)

def account(request):
    context = {}

    return render(request, 'website/account.html', context=context)

def events_and_promotions(request):
    context = {}

    return render(request, 'website/events_and_promotions.html', context=context)

def marathons(request):
    context = {}

    return render(request, 'website/marathons.html', context=context)

def repertoire(request):
    context = {}

    return render(request, 'website/repertoire.html', context=context)

def schools(request):
    context = {}

    return render(request, 'website/schools.html', context=context)