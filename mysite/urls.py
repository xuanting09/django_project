from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 使用 path 而不是 url
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]