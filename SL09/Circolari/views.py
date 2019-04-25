from django.http import HttpResponse,Http404
from .models import Circolare

def index(request):
    #return HttpResponse("Hello, world. You're at the Circolari index.")
    latest_circolari_list = Circolare.objects.order_by('DataPubblicazione')[:10000]
    output=""
    for i in latest_circolari_list:
        output = output + "Numero: %d"  %i.NumeroProgressivo +" %s"  %i.AnnoScolastico + ", Oggetto: " +  i.Oggetto
        output= output + ";\n" 
    return HttpResponse(output)

def detail(request, circolare_id):
    output=""
    try:
        i = Circolare.objects.get(pk=circolare_id)
        output = output + "Numero: %d"  %i.NumeroProgressivo +" %s"  %i.AnnoScolastico + ", Oggetto: " +  i.Oggetto
    except Circolare.DoesNotExist:
        raise Http404("Circolare non esiste")
    return HttpResponse(output)


