from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('a', include('blog.urls'))  # ''で始まるURLははblogアプリのurl.pyの引用
]
