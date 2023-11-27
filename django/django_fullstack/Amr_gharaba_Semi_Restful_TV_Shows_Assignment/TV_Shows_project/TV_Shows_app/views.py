from django.shortcuts import render,HttpResponse,redirect
from .models import Shows
from time import strftime, localtime
def root(request):
    content = {
        'shows' : Shows.objects.all()
    }
    return render(request,'index.html',content)
def tv_form(request):
    return render(request,'tv_form.html')

def tv_add(request):
    Shows.objects.create(title = request.POST['title'],release_date = request.POST['release_date'], network = request.POST['network'] , desc= request.POST['discription'] )
    request.session['id'] = Shows.objects.last().id
    return redirect(f'/shows/{Shows.objects.last().id}')
# Create your views here.

def show_detail(request, id):
    content = {
        'added_show': Shows.objects.get(id = id)
    }
    return render(request, 'show_detail.html', content)

def delete(request, id):
    Shows.objects.get(id = id).delete()
    return redirect('/shows')

def edit_form(request, id):
    content = {
        'edit_show': Shows.objects.get(id = id)
    }
    return render(request, 'show_edit.html', content)

def update(request, id):
    
    show = Shows.objects.get(id = id)
    if request.POST['title']:
        show.title = request.POST['title']
    if request.POST['release_date']:
        show.release_date = request.POST['release_date']
    if request.POST['network']:
        show.network = request.POST['network']
    if request.POST['discription']:
        show.desc = request.POST['discription']
    show.save()
    return redirect(f'/shows/{id}')