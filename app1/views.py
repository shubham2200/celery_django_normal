from django.shortcuts import render
from .task import *


# Create your views here.
def home(request):
    # sleepy.delay(10)
    return render(request , 'home.html')