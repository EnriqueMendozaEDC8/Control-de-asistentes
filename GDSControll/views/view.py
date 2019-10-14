from django.http import HttpResponse,HttpRequest
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render,render
from django.views.decorators.csrf import csrf_exempt

import datetime

def registro(request):
    print(request.POST)
    return render(request, 'registro.html', {})

def asistencia(request):
    print(request.POST)
    return render(request, 'asistencia.html', {})

@csrf_exempt
def confirmacion(request):
    print(request.POST)
    return render(request, 'confirmacion_registro.html', {})