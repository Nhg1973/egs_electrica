from django.shortcuts import render

def home(request):
    return render(request, 'publica/home.html')

def about(request):
    return render(request, 'publica/home/Nosotros.html')

def services(request):
    return render(request, 'publica/home/Servicios.html')

def testimonials(request):
    return render(request, 'publica/home/Opiniones.html')

def pricing(request):
    return render(request, 'publica/home/Productos.html')

def portfolio(request):
    return render(request, 'publica/home/Trabajos.html')

def blog(request):
    return render(request, 'publica/home/Ayudas.html')

def detalle(request):
    return render(request, 'publica/home/detalle_trabajo.html')

def contacto(request):
    return render(request, 'publica/home/contacto.html')

