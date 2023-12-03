from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import User ,Book
import bcrypt

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
            hash_pass = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            User.objects.create(first_name = request.POST['first_name'],last_name = request.POST['last_name'],email_address = request.POST['email_address'],password = hash_pass)
            request.session['id'] = User.objects.last().id
            messages.success(request, "User created Successfully")
            return redirect('/success')


    elif request.POST['which_form'] == 'login':
        print(User.objects.get(email_address = request.POST['email_address']).password)
        print('input password : ',bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode())
        if User.objects.filter(email_address = request.POST['email_address']) and bcrypt.checkpw(request.POST['password'].encode(), User.objects.get(email_address = request.POST['email_address']).password.encode()):
            request.session['id'] = User.objects.get(email_address = request.POST['email_address']).id
            return redirect('/success')
        else:
            messages.error(request, "Invalid email or password")
            return redirect('/')


def success(request):
    content = {
        'user' : User.objects.get(id = request.session['id']),
        'books' : Book.objects.all(),
        'users' : User.objects.all()
    }
    return render(request, 'welcome.html',content)

def logout(request):
    request.session.flush()
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
        'fav_users':User.objects.filter(fav_books = Book.objects.get(id = id)),
        'current_user' : User.objects.get(id = request.session['id']),
    }
    return render(request,'book_details.html',content)

def unfavorite(request,id):
    Book.objects.get(id = id).fav_users.remove(User.objects.get(id = request.session['id']))
    return redirect('/success')

def add_to_favorite(request,id):
    User.objects.get(id = request.session['id']).fav_books.add(Book.objects.get(id = id))
    return redirect('/success')

def update(request, id):
    
    errors = Book.objects.basic_validator(request.POST)
    if len(errors) > 0 :
            for key, value in errors.items():
                messages.error(request, value)
    else:
        book_update = Book.objects.get(id = id)
        book_update.desc = request.POST['desc']
        book_update.title = request.POST['title']
        book_update.save()
    return redirect(f'/book_details/{Book.objects.get(id = id).id}')

def delete(request, id):
    book_delete = Book.objects.get(id = id)
    book_delete.delete()
    return redirect('/success')