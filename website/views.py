from django.shortcuts import render


def main_page(request):
    context = {}

    return render(request, 'website/main.html', context=context)

def maratons(request):
    context = {}

    return render(request, 'website/maratons.html', context=context)

def schools(request):
    context = {}

    return render(request, 'website/schools.html', context=context)