from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("<h1> Hello la team</h1>")

def about(request):
    return HttpResponse("<h1> A PROPOS</h1>" "<p> wesh cousin c'est comment? </p>")

def listings(request):
    return HttpResponse("<h1> LISTINGS</h1>")

def contact(request):
    return HttpResponse("<h1> CONTACTEZ NOUS</h1>")