from django.shortcuts import render
from django.http import HttpResponse
from datetime import time


# Create your views here.

def selector(request):
    time = time.now()
    print time
    return render(request, 'generator.html')

def graphic(request):
    return render(request, 'graphic.html')