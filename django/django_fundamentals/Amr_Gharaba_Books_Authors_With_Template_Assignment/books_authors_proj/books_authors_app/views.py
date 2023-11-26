from django.shortcuts import render, HttpResponse,redirect
from .models import *

def root(request):
    content = {
        'books': Books.objects.all,
        'authors': Authors.objects.all(),
        }
    return render(request, 'index.html',content)

def add_book(request):
    Books.objects.create(title = request.POST['title'], desc = request.POST['description'])
    return redirect('/')
def add_author(request):
    Authors.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'])
    return redirect('/')

def book_detail(request, id):
    request.session['book_id'] = id
    print(request.session['book_id'])
    content = {
        'books': Books.objects.all,
        'book':Books.objects.get(id = request.session['book_id']),
        'authors': Authors.objects.all(),
        'exclude_author': Authors.objects.exclude(books = Books.objects.get(id = id)),
        }
    return render(request, 'book.html', content)

def author_detail(request, id):
    request.session['author_id'] = id
    content = {
        'books': Books.objects.all,
        'author':Authors.objects.get(id = request.session['author_id']),
        'authors': Authors.objects.all(),
        'exclude_book': Books.objects.exclude(author = Authors.objects.get(id = id))
        }
    return render(request, 'author.html', content)

def add_book_author(request):
    Authors.objects.get(id = request.session['author_id']).books.add(request.POST['book'])
    return redirect(f'/authors/{request.session['author_id']}')

def add_author_book(request):
    Books.objects.get(id = request.session['book_id']).author.add(request.POST['author'])
    return redirect(f'/books/{request.session['book_id']}')