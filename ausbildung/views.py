from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.

def home(request):
    h1 = "Übersicht der Themen"
    name = "Ingo"
    themen = Thema.objects.all()
    content = {
        'name': name,
        'themen': themen,
        'h1': h1,
    }
    return render(request, "index.html", content)