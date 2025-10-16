from django.shortcuts import render
from .models import Home, Client
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    
    home = Home.objects.filter(recomended=True)
    clients = Client.objects.all()
    
    return render(request, "index.html", {"home" : home, "clients": clients})

@login_required
def about_us(request):
    return render(request, 'about-us.html')

@login_required
def listings(request):
    return render(request, 'listings.html')

@login_required
def blog(request):
    return render(request, 'blog.html')

@login_required
def single_blog(request):
    return render(request, 'single-blog.html')

@login_required
def contact(request):
    return render(request, 'contact.html')