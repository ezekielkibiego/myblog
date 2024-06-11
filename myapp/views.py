from django.contrib import messages
from django.shortcuts import redirect, render
from .models import *
from .forms import BlogForm
# Create your views here.

def home(request):
    
    blogs = Blog.objects.all()
    
    context = {'blogs': blogs}
    return render(request, 'index.html', context)

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def subscriber(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Subscriber.objects.filter(email=email).exists():
            messages.error(request, 'You are already subscribed.')
        else:
            subscriber = Subscriber(email=email)
            subscriber.save()
            messages.success(request, 'Thank you for subscribing to our monthly newsletters!')
            return redirect('subscribe')
    return render(request, 'subscribe.html')



def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = BlogForm()
        
    context = {'form': form}
    return render(request, 'add_blog.html', context)
