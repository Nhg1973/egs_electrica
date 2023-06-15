
from django.contrib import admin
from django.urls import path

#importamos urls publica
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('publica.urls')),
]
