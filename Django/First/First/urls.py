from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Second/', include('Second.urls')),
    path('', include('Third.urls')),
    path('News/', include('news.urls')),
]

