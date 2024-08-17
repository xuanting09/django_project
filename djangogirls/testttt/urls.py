from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index/', views.index_view, name='index'),  # 主页
    path('about/', views.about, name='about'),
    path('blog-home/', views.blog_home, name='blog-home'),
    path('blog-post/', views.blog_post, name='blog-post'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('portfolio-item/', views.portfolio_item, name='portfolio-item'),
    path('portfolio-overview/', views.portfolio_overview, name='portfolio-overview'),
    path('pricing/', views.pricing, name='pricing'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
