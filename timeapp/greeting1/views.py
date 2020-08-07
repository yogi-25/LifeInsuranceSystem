from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hi(request):
    return HttpResponse('<h1> heloo hi this is my greetin  !111 g one view </h1>')
