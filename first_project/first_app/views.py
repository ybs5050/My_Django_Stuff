from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # Show html
    my_dict = {'insert_me' : 'Now I am coming from first_app/index.html!',
               'myname' : 'go'}
    return render(request, 'first_app/index.html', context = my_dict)

def index2(request):
    return HttpResponse("<em>My Second Aasdfsadfapp </em>")
