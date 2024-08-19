from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def about(request):
    return render(request, 'about.html')


def search(request):
    return render(request, 'search.html')

def home(request):
    return render(request, 'home.html')

def portfolio_item(request):
    return render(request, 'portfolio-item.html')

def portfolio_overview(request):
    return render(request, 'portfolio-overview.html')

def subscribe(request):
    return render(request, 'subscribe.html')

def index_view(request):
    return render(request, 'index.html')
