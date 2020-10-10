from django.shortcuts import render
from .models import *

def index(request) :
    courses = Course.objects.all()
    spots = Spot.objects.all()
    return render(request, "index.html", {'courses' : courses, 'spots':spots})
