from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    # path('',include('artical.urls')),
    path('artical/',include('artical.urls')),
    path('admin/', admin.site.urls),
]
