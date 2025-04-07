# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.http  import HttpResponse
#from appcastillocongosto.models import *
#from .models import *

'''
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger	#paginacion
from django.contrib.auth import authenticate, get_user_model, login,logout  #todas son por defecto
from django.contrib.auth.decorators import login_required
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.models import User
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

#email
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages

#curriculum con reportlab
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
import os

#para el chat
from django.http import JsonResponse
'''

from django.conf import settings
import os
from django.http import FileResponse, HttpResponseNotFound

# Create your views here.

################################################
# 1 - home
################################################

def home(request):
    nombre='Alfonso'
    context = {'nombre': nombre}
    return render(request, 'home.html', context=context)

################################################
# 2 - eL cASTILLO
################################################

def castillo(request):
    print("hola estoy en castillo")
    nombre='Alfonso'
    context = {'nombre': nombre}
    return render(request, 'castillo.html', context=context)

def sobremi(request):
    print("hola estoy en home")
    nombre='Alfonso'
    context = {'nombre': nombre}
    return render(request, 'home.html', context=context)


def Login(request):
    print("Login")
    request.user.username = nombre
    request.user.password = clave

    idUsuario = 0
    cUsuario = ""
    cUsuario = str(request.user)
    entrevistador = User.objects.get(username=cUsuario)
    nombreusuario = cUsuario
    idUsuario = entrevistador.id
    print("\nUSUARIO ACTIVO = " + str(request.user) + "\nID USUARIO ACTIVO = " + str(idUsuario))
    context = {'nombre': nombre, 'clave': clave, 'entrevistador': entrevistador}
    return render(request, 'home.html', context=context)


def login_view(request):
    print("Logi_view")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            actual = request.user  # usuario actual
            idusuario = 0
            idusuario = actual.id
            request.session['idusuario'] = idusuario
            print("idusuario=" + str(idusuario))
            entrevistador = Entrevistador.objects.get(user=idusuario)
            idEntrevistador = entrevistador.id
            print("idEntrevistador=" + str(idEntrevistador))
            print("FOTO=" + str(entrevistador.avatar))
            fotoperfil = settings.MEDIA_URL + str(
                entrevistador.avatar) if entrevistador.avatar else settings.MEDIA_URL + "MONEDA3.jpg"
            print("avatar=" + str(fotoperfil))
            context = {'fotoperfil': fotoperfil}
            return render(request, 'home.html', context=context)
            # return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login.html')

################################################
# El registro de usuarios
################################################
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('login')  # Redirige al login una vez registrado
    return render(request, 'register.html')

################################################
# 3 - mostrar pdf
################################################
def mostrar_pdf(request, filename):
    filepath = os.path.join(settings.BASE_DIR, 'pdfs', filename)

    # Verificamos si el archivo existe
    if not os.path.exists(filepath):
        return HttpResponseNotFound("Archivo no encontrado")

    # Usamos FileResponse directamente sin abrir el archivo con 'with open'
    response = FileResponse(open(filepath, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{filename}"'
    return response

################################################
# 2 - descargar pdf
################################################
def descargar_pdf(request, filename):
    # Asumimos que los archivos PDF están en la carpeta 'pdfs/' dentro del directorio de medios
    filepath = os.path.join(settings.BASE_DIR, 'pdfs', filename)
    print(str(filepath))

    # Verificamos si el archivo existe
    if not os.path.exists(filepath):
        return HttpResponseNotFound("Archivo no encontrado")

    # Usamos FileResponse directamente sin abrir el archivo con 'with open'
    response = FileResponse(open(filepath, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response