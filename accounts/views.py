from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        phone = request.POST.get("phone")
        password = request.POST.get("password")

        user = authenticate(request, phone=phone, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Tizimga muvaffaqiyatli kirdingiz!")
            return redirect("/")
        else:
            messages.error(request, "❌ Telefon yoki parol noto'g'ri!")
            return render(request, "accounts/auth.html")

    return render(request, "accounts/auth.html")


def logout_view(request):
    logout(request)
    return redirect("auth:login")
