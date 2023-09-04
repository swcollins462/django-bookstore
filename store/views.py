from django.shortcuts import render
from .models import Book


def index(request):
    return render(request, 'store/template.html')


def store(request):
    count = Book.objects.all().count()
    context = {
        'count': count,
    }
    return render(request, 'store/store.html', context)
