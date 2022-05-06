from django.shortcuts import render
from django.template import RequestContext


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
