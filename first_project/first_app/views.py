from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord

# Create your views here.

def index(request):
    # Show html
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records' : webpages_list}
    my_dict = {'insert_me' : 'Now I am coming from first_app/index.html!',
               'myname' : 'go'}
    return render(request, 'first_app/index.html', context = date_dict)

def index2(request):
    return HttpResponse("<em>My Second Aasdfsadfapp </em>")
