from django.shortcuts import render
from time import gmtime, strftime, localtime
    
def index(request):
    context = {
        "time_short": strftime("%Y-%m-%d %H:%M %p", localtime()),
        "time_long": strftime("%b-%d-%Y %H:%M %p", localtime())
    }
    return render(request,'index.html', context)

