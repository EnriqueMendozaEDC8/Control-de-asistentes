from django.http import HttpResponse,HttpRequest
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render,render
from django.views.decorators.csrf import csrf_exempt
from asistentes.models import Participantes,Asistencia
from datetime import date

import datetime

def registro(request):
    return render(request, 'registro.html', {})

def asistencia(request):
    return render(request, 'asistencia.html', {})

@csrf_exempt
def confirmacion(request):
    
    try:
        nombre = request.POST['nombres']
        apellido = request.POST['apellidos']
        telefono = request.POST['telefono']
        email = request.POST['email_participante']
        fecha_registro = date.today()
        existe = Participantes.objects.filter(email = email)
        if ( len(existe) == 0):
            participante = Participantes(nombres = nombre,apellidos = apellido,telefono = telefono,email = email,fecha_registro = fecha_registro)
            participante.save()
            numparticipante = participante.id
        else: 
            numparticipante = existe[0].id
    except:
        return render(request, 'registro.html', {})
    participante = Participantes.objects.get(id = numparticipante)
    asistencia = Asistencia.objects.filter(participante = numparticipante)
    if ( len(asistencia) == 0):
        asistencia = Asistencia(participante = participante,dia_uno = fecha_registro)
        asistencia.save()
    else:
        try:
            asistencia = Asistencia.objects.get(participante = participante)
            if(not asistencia.dia_dos):
                asistencia.dia_uno = fecha_registro
                asistencia.save()
        except:
            print("error en la ejecucion")
    return render(request, 'confirmacion_registro.html', {"numparticipante":numparticipante})


@csrf_exempt
def MarcarAsistencia(request):
    try:
        numeroUsuario = request.POST['numeroUsuario']
        asistencia = Asistencia.objects.get(participante = numeroUsuario)
        fecha_registro = date.today()
        if (not asistencia.dia_dos and fecha_registro != asistencia.dia_uno):
            asistencia.dia_dos = fecha_registro
            asistencia.save()
            return render(request, 'asistencia.html', {"mensaje":"El registro fue un exito"})
        if (not asistencia.dia_tres and fecha_registro != asistencia.dia_dos):
            asistencia.dia_tres = fecha_registro
            asistencia.save()
        return render(request, 'asistencia.html', {})
    except:
        return render(request, 'asistencia.html', {"mensaje":"Usted no se encuentra registrado"})