from django.http import HttpResponse
from django.shortcuts import render
from .form import Contact

def form(request):
    if request.method == "GET":
        form = Contact({
            'first_name': 'Valentina',
            'last_name': 'Duque',
            'message': 'Hola tonotos',
            'subject': 'No se'
        })
        return render(request, 'formulario.html', {
            'formulario': form
        })
    if request.method == "POST":
        form = Contact(request.POST)
        #acciones a realizar si el formulario es valido
        if form.is_valid():
            return HttpResponse('Formulario por post')
        #acciones a realizar si el formulario no es valido
        else:
            return render(request, 'formulario.html', {
            'formulario': form
        })
    

# def 