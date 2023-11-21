from django.shortcuts import render,HttpResponse,redirect
from .models import users
def index(request):
    content  ={'users':users.objects.all()}
    # request.session['content'] = content
    return render(request, 'index.html', content)

def add_user(request):
    firstName = request.POST['first_name']
    lastName = request.POST['last_name']
    Email = request.POST['email']
    Age = request.POST['age']
    users.objects.create(first_name = firstName, last_name=lastName, email_address = Email, age = Age)
    return redirect('/')
