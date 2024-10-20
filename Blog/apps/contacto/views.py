from django.shortcuts import redirect, render
from .forms import ContactForm
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.contrib import messages

def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            subject = 'this is a subject'
            contenido = f'Hola {nombre} {apellido}. Tu dirección de correo {email} es correcta?'
            recipient_list=[email]
            from_email = settings.EMAIL_HOST_USER
            mensaje= EmailMessage(
                subject,
                contenido,
                from_email,
                recipient_list
            )

            try:
                mensaje.send()
                print("enviado")
                return render(request, 'contacto/contacto.html', {'enviado':1})
            except:
                print("no enviado")
                return render(request, 'contacto/contacto.html', {'enviado':0})
    else:
        form = ContactForm()
    return render(request, 'contacto/contacto.html', {'form':form ,'enviado':None})