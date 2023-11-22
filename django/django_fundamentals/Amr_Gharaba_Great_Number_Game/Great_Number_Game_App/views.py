from django.shortcuts import render,HttpResponse,redirect
import random

def index(request):
        request.session['randomNumber'] = random.randint(1,100)
        request.session['number'] = 'number'
        request.session['submit']  = 'submit'
        request.session['guesses']=0
        content = {'playAgain': 'hidden', 'number':request.session['number'],'submit':request.session['submit'],'guesses':request.session['guesses']}    
        return render(request,'index.html',content)


def submit(request):
    if not request.POST['number']:
        guess = 'invalid input'
        style = 'red'
        playAgain = 'hidden'
    else:
        request.session['inputNumber'] = int(request.POST['number'])
        if request.session['inputNumber'] == request.session['randomNumber']:
            guess = f'{request.session['inputNumber']} was the number'
            style = 'green'
            playAgain = 'submit'
            request.session['number'] = 'hidden'
            request.session['submit']  = 'hidden'
        elif request.session['inputNumber'] > request.session['randomNumber']:
            guess = 'Too High'
            style = 'red'
            playAgain = 'hidden'
            request.session['guesses']+=1
        else:
            guess = 'Too Low'
            style = 'red'
            playAgain = 'hidden'
            request.session['guesses']+=1
    print(request.session['inputNumber'])
    print(request.session['randomNumber'])
    content = {'string': guess, 'style':style, 'playAgain':playAgain,'number':request.session['number'],'submit':request.session['submit'], 'guesses':request.session['guesses']}
    return render(request,'index.html',content)
    # return redirect('/',content)

# Create your views here.
