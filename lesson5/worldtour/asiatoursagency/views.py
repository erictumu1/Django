from django.shortcuts import render
from .models import Tour #The . means import from the current directory.

# Create your views here.
def index(request):
    tours = Tour.objects.all() #This brings all instances of the Tour class and stores them into tours.
    context = {'tours':tours} #This is a dictionary to store all the tours.
    return render(request, 'tours/index.html',context)