from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Nombre',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresá tu nombre', 'required': True})
    )
    email = forms.EmailField(
        label='Email',
        max_length=100,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingresá una dirección de correo', 'required': True})
    )
    subject = forms.CharField(
        label='Motivo',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Asunto', 'required': True})
    )
    message = forms.CharField(
        label='Mensaje',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'En qué podemos ayudarte ', 'required': True})
    )


class PresupuestoForm(forms.Form):
    subject_choices = (
    ('', 'Seleccioná una opción'),
    ('Insumos electricos', 'Insumos eléctricos'),
    ('servicio_instalacion', 'Servicio de instalación'),
    ('servicio_cableado', 'Servicio de cableado'),
    ('Asesoramiento', 'Asesoramiento'),
    ('Otra consulta', 'Otra consulta'),
)

    name = forms.CharField(
        label='Nombre',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresá tu nombre', 'required': True})
    )
    email = forms.EmailField(
        label='Email',
        max_length=100,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingresá tu dirección de correo', 'required': True})
    )


    subject = forms.ChoiceField(
        label='Producto o Servicio',
        choices=subject_choices,
        widget=forms.Select(attrs={'class': 'form-control', 'required': True})
    )


    message = forms.CharField(
        label='Mensaje',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mensaje', 'required': False})
    )
