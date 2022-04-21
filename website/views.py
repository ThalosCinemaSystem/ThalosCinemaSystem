from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    context = {}

    return render(request, 'website/main.html', context=context)