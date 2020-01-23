from django.http import HttpResponse,HttpRequest
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render,render
from django.views.decorators.csrf import csrf_exempt
from django import db

from asistentes.models import Participantes,Asistencia,Recursos,Rol
from datetime import date

import datetime,re

def menu(request):
    return render(request, 'menu.html', {})
    
def registro(request):
    roles = Rol.objects.all()
    return render(request, 'registro.html', {'roles':roles})

def asistencia(request):
    return render(request, 'asistencia.html', {})

def recursos(request):
    try:
        recursos = Recursos.objects.all().order_by('tema')
        return render(request, 'recursos.html', {'recursos': recursos})
    except:
        return render(request, 'recursos.html', {})

@csrf_exempt
def confirmacion(request):
    try:
        if is_email(request.POST['email_participante']) and is_name(request.POST['nombres']) and is_name(request.POST['apellidos']):
            return render(request, 'registro.html', {})
        nombre = request.POST['nombres']
        apellido = request.POST['apellidos']
        telefono = str(request.POST['telefono'])
        email = request.POST['email_participante']
        rol = Rol.objects.get(id = request.POST['rol'])
        fecha_registro = date.today()
        existe = Participantes.objects.filter(email = email)
        if not request.POST['telefono'].isnumeric():
            roles = Rol.objects.all()
            return render(request, 'registro.html', {'roles':roles})
        if ( len(existe) == 0):
            participante = Participantes(nombres = nombre,apellidos = apellido,telefono = telefono,email = email,fecha_registro = fecha_registro,rol=rol)
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
            return render(request, 'asistencia.html', {"mensaje":"Se realizo registro de su asustencia"})
        if (not asistencia.dia_tres and fecha_registro != asistencia.dia_dos):
            asistencia.dia_tres = fecha_registro
            asistencia.save()
        return render(request, 'asistencia.html',{})
    except:
        return render(request, 'asistencia.html', {"mensaje":"Usted no se encuentra registrado"})

def is_name(name):
    if len(name)<4 or len(name)> 40:
        return False
    expresion_regular = r"/^[A-Za-z\s]+$/g"
    return re.match(expresion_regular, name) is not None

def is_phone(phone):
    if len(phone)<7 and len(phone)>15:
        return False
    return True

def is_email(correo):
    if len(correo)<10 or len(correo)> 60:
        return False
    expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(expresion_regular, correo) is not None