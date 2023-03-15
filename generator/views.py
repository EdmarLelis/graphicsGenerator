from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.

def selector(request):
    time = datetime.now()
    print(time)
    return render(request, 'generator.html')

def graphic(request):
    return render(request, 'graphic.html')