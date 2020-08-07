from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def hello_world(request):
    date = datetime.datetime.now()
    s = '<h1> Heloo im shwoing current date and time <h1> <body>Date and time is: '+str(date)+'</body>'
    return HttpResponse(s)
def hi(request):
    return HttpResponse('<h1> heloo hi this is my new view </h1>')
