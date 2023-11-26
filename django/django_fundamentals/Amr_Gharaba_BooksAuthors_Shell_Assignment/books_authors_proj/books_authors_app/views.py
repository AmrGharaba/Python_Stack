from django.shortcuts import render, HttpResponse

def root(request):
    return HttpResponse('hello')

# Create your views here.
