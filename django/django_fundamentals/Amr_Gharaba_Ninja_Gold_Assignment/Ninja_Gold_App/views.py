from django.shortcuts import render, redirect, HttpResponse
import random
from time import strftime, localtime

def root(request): 
    # request.session['Gold'] = 0
    # request.session['time_stamp'] = []
    return render(request, 'index.html')

def quest(request):
    time = strftime("%B %d %Y %H:%M %p", localtime())
    if 'Gold' not in request.session: request.session['Gold'] = 0
    else:
        print(request.POST["which_form"])
        if request.POST["which_form"] != 'Quest':
            random_number = random.randint(10,20)
            request.session['Gold'] += random_number
        else: 
            random_number = random.randint(-50,50)
            request.session['Gold']  += random_number

    ### creating time stamp array session   
    if 'time_stamp' not in  request.session: request.session['time_stamp'] = []
    else: 
        if request.POST["which_form"] !='Quest':
            string = f'You entered a {request.POST["which_form"]} and earned {random_number} gold. ({time})'
            request.session['time_stamp'].append(string)
        else:
            if random_number > 0:
                string = f'You completed a {request.POST["which_form"]} and earned {random_number} gold. ({time})'
            else: 
                string = f'You failed a {request.POST["which_form"]} and lost {abs(random_number)} gold. Ouch. ({time})'
            request.session['time_stamp'].append(string)
    print(request.session['time_stamp'])
    return redirect('/')
def reset(request):
    request.session['time_stamp'] = []
    request.session['Gold'] = 0
    return redirect('/')






