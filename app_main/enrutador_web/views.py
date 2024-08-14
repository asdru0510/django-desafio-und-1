from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("estoy en HOME")

def contact(request):
    return HttpResponse("estoy en contact")

def about(request):
    return HttpResponse("estoy en about")