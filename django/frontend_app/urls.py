from django.urls import path
from .views import SomeProtectedView
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin

urlpatterns = [
    path('protected/', SomeProtectedView.as_view(), name='protected'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # 使用已上传的 login.html
    path('index/', views.index_view, name='index'),  # 渲染 index.html
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('home/', views.home, name='home'),  # 渲染 strategy_section.html
    path('portfolio-item/', views.portfolio_item, name='portfolio-item'),
    path('portfolio-overview/', views.portfolio_overview, name='portfolio-overview'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('admin/', admin.site.urls),
]
