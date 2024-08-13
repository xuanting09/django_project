from django.contrib import admin
from django.urls import path
from myapp import views
from myapp import views

urlpatterns = [
    # 使用 path 而不是 url
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),  # 新增的 home 視圖 URL

]
