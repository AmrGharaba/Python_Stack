from django.shortcuts import render, HttpResponse, redirect
from .models import Dojo, Ninja
def root(request):
    content = {
        'dojos' : Dojo.objects.all()
    }
    return render(request,'index.html',content)

def dojo(request):
    Dojo.objects.create(name = request.POST['name'], city = request.POST['city'], state = request.POST['state'])

    return redirect('/')

def ninja(request):
    Ninja.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], dojo = Dojo.objects.get(name = request.POST['dojo']))

    return redirect('/')

def delete(request,dojo):
    Dojo.objects.get(name = dojo).delete()
    return redirect('/')