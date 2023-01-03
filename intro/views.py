from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    about=About.objects.first()
    skills=Skills.objects.all()
    education=Education.objects.all()
    exp=Experience.objects.all()
    port=portfolio.objects.all()
    service=Service.objects.all()
    return render(request,'index.html',{'about':about,'skills':skills,'education':education,'exp':exp,'port':port,'service':service})