from django.shortcuts import render, HttpResponse, redirect
def root(request):
    return HttpResponse('hello')

# Create your views here.
