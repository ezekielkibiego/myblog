from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    
    blogs = Blog.objects.all()
    
    context = {'blogs': blogs}
    return render(request, 'index.html', context)

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

