from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Film

# Create your views here.

def index(request):
    latest_film_list = Film.objects.order_by('annoUscita')[:30]
    template = loader.get_template('Film/index.html')
    context = {
        'latest_film_list' : latest_film_list
    }
    return HttpResponse(template.render(context, request))
    #output = '<br> '.join([f.titolo for f in latest_film_list])
    #return HttpResponse(output)

def detail(request, film_id):
    return HttpResponse("")