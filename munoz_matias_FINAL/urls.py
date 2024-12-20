from django.contrib import admin
from django.urls import path, include
from app_seminario.views import index  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('seminario/', include('app_seminario.urls')),  
]
