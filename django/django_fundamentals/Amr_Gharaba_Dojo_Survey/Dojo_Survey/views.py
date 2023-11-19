from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def result(request):
    print(request.POST)
    name = request.POST['name']
    location = request.POST['location']
    favorite = request.POST['favorite_language']
    comment = request.POST['comment']

    context = {
        'name': name,
        'location' : location,
        'favorite': favorite,
        'comment': comment

    }
    return render(request,'result.html', context)

# Create your views here.
