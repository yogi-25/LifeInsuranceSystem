from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hi(request):
    return HttpResponse('<h1> heloo hi this is my greeting view </h1>')
