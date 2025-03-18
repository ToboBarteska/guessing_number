from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("ahoj negře🐒")

def problem(request, promena,cena ):
    return HttpResponse(f"Zboží: {promena} {cena}")

def pohoda(request):
    return HttpResponse("Nemam, pohoda")