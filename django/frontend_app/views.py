from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib import admin
from .models import SecurityNews
from django.shortcuts import render
from .models import SecurityNews


@admin.register(SecurityNews)
class SecurityNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'url')

class SomeProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'protected.html'



def index_view(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def search(request):
    return render(request, 'search.html')
def home(request):
     # 取得所有新聞，按照發布日期的降序排列
    news = SecurityNews.objects.all().order_by('-publish_date')
    # 獲取搜尋條件
    query = request.GET.get('query', '')
    search_type = request.GET.get('search_type', '')

    # 根據搜尋類型進行過濾
    if search_type == 'title':
        news = SecurityNews.objects.filter(title__icontains=query)
    elif search_type == 'cve-id':
        news = SecurityNews.objects.filter(title__icontains=query)
    elif search_type == 'product-name':
        news = SecurityNews.objects.filter(content__icontains=query)
    else:
        # 如果沒有搜尋條件，返回所有新聞
        news = SecurityNews.objects.all().order_by('-publish_date')

    # 將搜尋結果和查詢內容傳回模板
    return render(request, 'home.html', {'news': news, 'query': query, 'search_type': search_type})

def portfolio_item(request):
    return render(request, 'portfolio-item.html')
def portfolio_overview(request):
    return render(request, 'portfolio-overview.html')
def subscribe(request):
    return render(request, 'subscribe.html')
def some_protected_view(request):
    return render(request, 'protected.html')
