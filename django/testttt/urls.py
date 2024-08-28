from django.urls import path
from . import views
from .views import SomeProtectedView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('protected/', SomeProtectedView.as_view(), name='protected'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('index/', views.index_view, name='index'),  # 主页
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('home/', views.home, name='home'),
    path('portfolio-item/', views.portfolio_item, name='portfolio-item'),
    path('portfolio-overview/', views.portfolio_overview, name='portfolio-overview'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('search/cveid/', views.cve_search, name='cve_search'),
    path('cve/<str:cve_id>/', views.cve_search, name='cve_search'),
]
