from django.urls import path
from . import views

app_name = 'publica'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('pricing/', views.pricing, name='pricing'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('presupuesto/', views.presupuesto, name='presupuesto'),
    path('detalle/<int:producto_id>/', views.detalle, name='detalle'),
    path('contacto/', views.contacto, name='contacto'),
     path('mostrar_producto/<int:producto_id>/', views.mostrar_producto, name='mostrar_producto'),
]

