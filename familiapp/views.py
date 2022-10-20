from django.shortcuts import render
from datetime import datetime
from django.shortcuts import render
from .models import Persona

# Create your views here.

def mostrar(request):
    data = {
        'data' : Persona.objects.all(),
    }
    return render(request, 'mostrar.html', data)

def crear(request, dni, nombre, apellido):
    persona = Persona(nombre = nombre, apellido = apellido, dni = dni, alta = datetime.now())
    persona.save()

    data = {
        'titulo' : 'Familiar creado',
        'subtitulo' : apellido + ', ' + nombre,
    }
    return render(request, 'crear.html',data)

# Create your views here.

"hola esto despues borralo"
