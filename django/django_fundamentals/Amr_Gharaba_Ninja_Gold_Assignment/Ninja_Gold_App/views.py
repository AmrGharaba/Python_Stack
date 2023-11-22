from django.shortcuts import render, redirect, HttpResponse
import random
from time import strftime, localtime

def root(request): 
    return render(request, 'index.html',request.session['content'])

def quest(request):
    time = strftime("%B %d %Y %H:%M %p", localtime())
    if request.session['content']['Gold']:
        print(request.POST["which_form"])
        if request.POST["which_form"] == 'Farm' or request.POST["which_form"] == 'Cave' or request.POST["which_form"] == 'House':
            random_number = random.randint(10,20)
            request.session['content']['Gold'] += random_number
        else: 
            random_number = random.randint(-50,50)
            request.session['content']['Gold']  += random_number
    else: request.session['content'] =0
    ### creating time stamp array session   
    if 'time_stamp' not in  request.session: request.session['time_stamp'] = []
    else: 
        if request.POST["which_form"] !='Quest':
            string = f'You entered a {request.POST["which_form"]} and earned {random_number} gold. ({time})'
            request.session['time_stamp'].append(string)
            font_color = 'green'
        else:
            if random_number > 0:
                string = f'You completed a {request.POST["which_form"]} and earned {random_number} gold. ({time})'
                font_color = 'green'
            else: 
                string = f'You failed a {request.POST["which_form"]} and lost {abs(random_number)} gold. Ouch. ({time})'
                font_color = 'red'
            request.session['time_stamp'].append(string)
    print(request.session['time_stamp'])
    request.session['content'] = {
        'Gold': request.session['content']['Gold'],
        'font_color': font_color,
    }
    return redirect('/')







