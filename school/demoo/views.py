from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from .models import Team

# Create your views here.
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def details(request):
    return render(request,'details.html')
def home(request):
    return HttpResponse('welcome')
def tanks(request):
    return HttpResponse('thank you for vist this page')


def add(request):
    return render(request,'add.html')

def result(request):
    # x=int(request.GET['num1'])
    # y =int(request.GET['num2'])
    # add=x+y
    return render(request,'result.html')



def index(request):
    obj=Place.objects.all()
    ob=Team.objects.all()
    return render(request,'index.html',{'result':obj,'pln':ob})