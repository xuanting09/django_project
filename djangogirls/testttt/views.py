from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def about(request):
    return render(request, 'about.html')

def blog_home(request):
    return render(request, 'blog_home.html')

def blog_post(request):
    return render(request, 'blog_post.html')

def contact(request):
    return render(request, 'contact.html')

def faq(request):
    return render(request, 'faq.html')

def portfolio_item(request):
    return render(request, 'portfolio-item.html')

def portfolio_overview(request):
    return render(request, 'portfolio-overview.html')

def pricing(request):
    return render(request, 'pricing.html')

def index_view(request):
    return render(request, 'index.html')
