from django.shortcuts import render
from .models import Book


def index(request):
    context = {
        'page': 'Mystery Books',
        'menu_item': 'index',
    }
    return render(request, 'store/template.html', context)


def store(request):
    books = Book.objects.all()
    count = books.count()
    context = {
        'count': count,
        'books': books,
        'page': 'Welcome to Mystery Books',
        'menu_item': 'store',
    }
    return render(request, 'store/store.html', context)


def display_book(request, book_id):
    context = {
        'page': 'TEST' + str(book_id),
        'menu_item': 'TEST' + str(book_id),
    }
    return render(request, 'store/template.html', context)
