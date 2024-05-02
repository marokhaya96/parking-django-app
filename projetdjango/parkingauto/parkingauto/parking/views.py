from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("bonjour et bienvenue dans votre parking automobile.")