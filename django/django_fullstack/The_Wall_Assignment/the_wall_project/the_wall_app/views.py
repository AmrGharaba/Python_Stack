from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import User, Message, Comment
import bcrypt


def root(request):
    return render(request, 'index.html')

def user_processing(request):
    if request.POST['which_form'] == 'Register':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0 :
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            hash_pass = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            User.objects.create(first_name = request.POST['first_name'],last_name = request.POST['last_name'],email_address = request.POST['email_address'],password = hash_pass)
            request.session['login_id'] = User.objects.last().id
            messages.success(request, "User created Successfully")
            return redirect('/user_interface')


    elif request.POST['which_form'] == 'login':
        
        if User.objects.filter(email_address = request.POST['email_address']) and bcrypt.checkpw(request.POST['password'].encode(), User.objects.get(email_address = request.POST['email_address']).password.encode()):
            request.session['login_id'] = User.objects.get(email_address = request.POST['email_address']).id
            return redirect('/user_interface')
        else:
            messages.error(request, "Invalid email or password")
            return redirect('/')

def user_interface(request):
    content = {
        'current_user' : User.objects.get(id = request.session['login_id']),
        'messeges': Message.objects.all(),
        }
    return render(request,'wall.html',content)

def log_out(request):
    request.session.flush()
    return redirect('/')

def post_message(request):
    errors = Message.objects.basic_validator(request.POST)
    if len(errors) > 0 :
        for key, value in errors.items():
            messages.error(request, value)
    else:
        Message.objects.create(message = request.POST['message'], user = User.objects.get(id = request.session['login_id']))

    return redirect('/user_interface')

def add_comment(request, id):
    Comment.objects.create(comment = request.POST['comment'], message = Message.objects.get(id = id), user = User.objects.get(id = request.session['login_id']))
    return redirect('/user_interface')

def delete_message(request, id):
    Message.objects.get(id = id).delete()
    return redirect('/user_interface')
