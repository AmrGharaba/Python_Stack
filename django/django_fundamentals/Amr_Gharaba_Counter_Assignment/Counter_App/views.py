from django.shortcuts import render,HttpResponse,redirect

def index(request):

    if 'count' in request.session:
        request.session['count']+=1
    else:
        request.session['count']=1
    dict = {'count':request.session['count']}
    return render(request,'index.html',dict)
def reset(request):
    request.session['count']=0
    return redirect('/')
def plus2(request):
    request.session['count']+=1
    return redirect('/')
    

# Create your views here.
