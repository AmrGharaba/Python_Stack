from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import Shows
from time import strftime, localtime
def root(request):
    return redirect('/shows')
def shows(request):
    content = {
        'shows' : Shows.objects.all()
    }
    return render(request,'index.html',content)
def tv_form(request):
    return render(request,'tv_form.html')

def tv_add(request):
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            print(messages.error(request, value))
        return redirect('/shows/tv_form')
    else:
        Shows.objects.create(title = request.POST['title'],release_date = request.POST['release_date'], network = request.POST['network'] , desc= request.POST['desc'] )
        messages.success(request, "Show successfully created")
        request.session['id'] = Shows.objects.last().id
        return redirect(f'/shows/{Shows.objects.last().id}')

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

    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
    else:
        show = Shows.objects.get(id = id)
        show.title = request.POST['title']
        show.release_date = request.POST['release_date']
        show.network = request.POST['network']
        show.desc = request.POST['desc']
        show.save()
        messages.success(request, "Show successfully updated")
    return redirect(f'/shows/{id}')