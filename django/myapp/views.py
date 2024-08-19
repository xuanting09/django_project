from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # 登入成功後的重定向
        else:
            messages.error(request, '帳號或密碼錯誤')
    return render(request, 'login.html')

def home_view(request):
    return render(request, 'home.html')