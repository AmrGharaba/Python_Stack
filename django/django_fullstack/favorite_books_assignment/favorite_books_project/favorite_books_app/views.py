from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import User ,Book

def root(request):
    return render(request,'index.html')

# Create your views here.
def processing(request):
    
    if request.POST['which_form'] == 'Register':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0 :
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            User.objects.create(first_name = request.POST['first_name'],last_name = request.POST['last_name'],email_address = request.POST['email_address'],password = request.POST['password'])
            request.session['id'] = User.objects.last().id
            request.session['action'] = 'Registered'
            messages.success(request, "User created Successfully")
            return redirect('/success')


    elif request.POST['which_form'] == 'login':
        if User.objects.filter(email_address = request.POST['email_address']) and User.objects.get(email_address = request.POST['email_address']).password == request.POST['password']:
            request.session['id'] = User.objects.get(email_address = request.POST['email_address']).id
            request.session['action'] = 'Logged in'
            return redirect('/success')
        else:
            messages.error(request, "Invalid email or password")
            return redirect('/')


def success(request):
    content = {
        'user' : User.objects.get(id = request.session['id']),
        'action' : request.session['action'],
        'books' : Book.objects.all(),
        'users' : User.objects.all()
    }

    return render(request, 'welcome.html',content)

def logout(request):
    request.session['id'] = False
    request.session['action'] = 'Logged out'
    return redirect('/')

def add_book(request):
    errors = Book.objects.basic_validator(request.POST)
    if len(errors) > 0 :
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/success')
    else:
        Book.objects.create(title = request.POST['title'], desc = request.POST['desc'], my_user = User.objects.get(id = request.session['id']))
        User.objects.get(id = request.session['id']).fav_books.add(Book.objects.last())
    return redirect('/success')

def book_details(request,id):
    content = {
        'book': Book.objects.get(id = id),
        'fav_users':User.objects.filter(fav_books = Book.objects.get(id = id))
    }
    
    if User.objects.get(books = Book.objects.get(id = id)).id == request.session['id']:
        content['display'] = 'show'
    else: content['display'] = 'none'
    return render(request,'book_details.html',content)
def unfavorite(request,id):
    Book.objects.get(id = id).fav_users.remove(User.objects.get(id = request.session['id']))
    return redirect('/success')
