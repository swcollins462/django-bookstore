from django.shortcuts import render


def index(request):
    return render(request, 'store/template.html')


def store(request):
    return render(request, 'store/store.html')
