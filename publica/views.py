import json
import os
import codecs
from django.contrib import messages
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render, get_object_or_404
from django.core.mail import send_mail

from publica.form.forms import ContactForm, PresupuestoForm


def home(request):
    return render(request, 'publica/home.html')

def about(request):
    return render(request, 'publica/home/Nosotros.html')

def services(request):
    return render(request, 'publica/home/Servicios.html')


from django.shortcuts import render

def pricing(request):
    # Ruta del archivo JSON de productos
    json_file_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),  # Directorio base del proyecto
        'publica',
        'data',
        'productos.json'
    )
    
    with codecs.open(json_file_path, 'r', 'utf-8') as json_file:
        data = json.load(json_file)

    # Acceder a las categorías
    categorias = data['categorias']

    context = {
        'categorias': categorias
    }

    return render(request, 'publica/home/Productos.html', context)


def portfolio(request):
    return render(request, 'publica/home/Trabajos.html')

def presupuesto(request):
    if request.method == 'POST':
        form = PresupuestoForm(request.POST)
        if form.is_valid():
            # Aquí puedes realizar acciones con los datos del formulario, como enviar correos electrónicos o guardar en la base de datos
            # Por ejemplo, puedes acceder a los campos de la siguiente manera:
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                # Procesar el envío del correo electrónico
                send_mail(subject, message, name, ['egselectricidadweb@gmail.com'], fail_silently=False)
                messages.success(request, f"{name} tu solicitud de presupuesto se envió exitosamente.")
            except:
                messages.error(request, 'Hubo un error al enviar el correo.')

            return redirect('publica:contacto')

    else:
        form = PresupuestoForm()
        
    return render(request, 'publica/home/presupuesto.html', {'form': form})



def detalle(request, producto_id):
    # Leer los datos del archivo JSON
    with codecs.open('publica/data/productos.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Buscar el producto según el identificador
    producto = None
    for categoria in data["categorias"]:
        for p in categoria["productos"]:
            if p["id"] == producto_id:
                producto = p
                break
        if producto:
            break

    # Verificar si se encontró el producto
    if not producto:
        return HttpResponseNotFound("El producto no existe")

    # Pasar el producto al contexto
    context = {
        'producto': producto
    }

    return render(request, 'publica/home/detalle_trabajo.html', context)

#este metodo es para enviar el mail con los datso del producto seleccionado

def mostrar_producto(request, producto_id):
    with open('publica/data/productos.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Buscar el producto según el identificador
    producto = None
    for categoria in data["categorias"]:
        for p in categoria["productos"]:
            if p["id"] == producto_id:
                producto = p
                break
        if producto:
            break

    # Verificar si se encontró el producto
    if not producto:
        return HttpResponseNotFound("El producto no existe")

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Procesar los datos del formulario válido
            nombre = form.cleaned_data['name']
            email = form.cleaned_data['email']
            asunto = form.cleaned_data['subject']
            mensaje = form.cleaned_data['message']

            # Redirigir al usuario a una página de éxito o a otra vista
            return redirect('publica:contacto')
    else:
        # Obtener los valores seleccionados de los campos <select>
        variedades = {}
        if 'atributos' in producto:
            for atributo in producto['atributos']:
                valor_seleccionado = request.GET.get(atributo['nombre'])
                if valor_seleccionado:
                    variedades[atributo['nombre']] = valor_seleccionado

        # Crear el formulario y establecer los valores iniciales
        form = ContactForm()
        form.initial = {'message': '\n'.join([f'{key}: {value}' for key, value in variedades.items()])}

    context = {
        'producto': producto,
        'seleccion': variedades,
        'form': form
    }
    return render(request, 'publica/home/mostrar_producto.html', context)




def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            message += f"\n\nCorreo electrónico: {email}\nNombre: {name}"
            try:
                # Procesar el envío del correo electrónico
                send_mail(subject, message, name, ['egselectricidadweb@gmail.com'], fail_silently=False)
                messages.success(request, f"{name} Tu correo se envió exitosamente.")
            except:
                messages.error(request, 'Hubo un error al enviar el correo.')

            return redirect('publica:contacto')
    else:
        form = ContactForm()

    return render(request, 'publica/home/contacto.html', {'form': form})






