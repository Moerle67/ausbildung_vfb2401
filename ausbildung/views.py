from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.

def gruppe(request):
    anzahl = Gruppe.objects.all().count()
    return HttpResponse(f"<h1>{anzahl} Gruppen angelegt</h1>")