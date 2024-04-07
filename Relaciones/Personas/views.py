from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .form import Formulario1

# Create your views here.

def form1(request):
    if request.method == 'GET':
        form_1 = Formulario1({
            'tipo': 'Tipo de documento',
        })
        return render (request, 'formulario1.html', {
        'formulario1': form_1
        })