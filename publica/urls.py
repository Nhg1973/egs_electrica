from django.urls import path
from . import views

app_name = 'publica'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('pricing/', views.pricing, name='pricing'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('blog/', views.blog, name='blog'),
    path('detalle/', views.detalle, name='detalle'),
    path('contacto/', views.contacto, name='contacto'),
]

