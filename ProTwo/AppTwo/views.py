from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    a = "<p>asdfasdfdsafdsafdsaf</p"
    return HttpResponse("<em>My Second App </em>" + a)

def help(request):
    helpdict = {'help_insert' : 'HELP PAGE'}
    return render(request, 'AppTwo/help.html', context = helpdict)

def next(request):
    helpdict = {'help_insert' : 'HELP PAGE'}
    return render(request, 'AppTwo/next.html', context = helpdict)
