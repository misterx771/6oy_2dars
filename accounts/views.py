from django.shortcuts import render
from django.contrib.auth import authenticate, login

def login_view(request):
    
    if request.POST:
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        user = authenticate(phone=phone, password=password)
        if user:
            login(request, user)
    
    return render(request, "accounts/auth.html")
