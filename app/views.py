from django.shortcuts import render

# Create your views here.
from app.models import *

def country(request):
    QLCO=Country.objects.all()
    d={ 'data':QLCO }

    return render(request,'country.html',d)

def state(request):
    QLSO=State.objects.all()
    d={ 'data1':QLSO }

    return render(request,'state.html',d)
