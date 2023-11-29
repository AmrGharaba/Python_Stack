from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import Users

def root(request):
    return render(request,'index.html')

# Create your views here.
def processing(request):
    
    if request.POST['which_form'] == 'Register':
        errors = Users.objects.basic_validator(request.POST)
        if len(errors) > 0 :
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            Users.objects.create(first_name = request.POST['first_name'],last_name = request.POST['last_name'],email_address = request.POST['email_address'],password = request.POST['password'],confirm_password = request.POST['confirm_password'])
            request.session['id'] = Users.objects.last().id
            request.session['action'] = 'Registered'
            messages.success(request, "User created Successfully")
            return redirect('/success')


    elif request.POST['which_form'] == 'login':
        if Users.objects.filter(email_address = request.POST['email_address']) and Users.objects.get(email_address = request.POST['email_address']).password == request.POST['password']:
            request.session['id'] = Users.objects.get(email_address = request.POST['email_address']).id
            request.session['action'] = 'Logged in'
            return redirect('/success')
        else:
            messages.error(request, "Invalid email or password")
            return redirect('/')


def success(request):
    content = {
        'user' : Users.objects.get(id = request.session['id']),
        'action' : request.session['action']
    }
    return render(request, 'welcome.html',content)

def logout(request):
    request.session['id'] = False
    request.session['action'] = 'Logged out'
    return redirect('/')