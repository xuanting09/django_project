from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class SomeProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'protected.html'


def index_view(request):
    return render(request, 'index.html')

@login_required
def about(request):
    return render(request, 'about.html')

@login_required
def search(request):
    return render(request, 'search.html')


def cve_search(request, cve_id):
    # 根據cve_id來查找相關數據
    # 將數據傳遞給模板進行渲染
    context = {'cve_id': cve_id}
    return render(request, 'cve_search.html', context)


@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def portfolio_item(request):
    return render(request, 'portfolio-item.html')

@login_required
def portfolio_overview(request):
    return render(request, 'portfolio-overview.html')

@login_required
def subscribe(request):
    return render(request, 'subscribe.html')

@login_required
def some_protected_view(request):
    return render(request, 'protected.html')

