from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('testttt.urls')),  # 如果這是主應用
    # path('myapp/', include('myapp.urls')),  # 如果需要包括 myapp
]
