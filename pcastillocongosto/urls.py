# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.urls import path,include,re_path
from appcastillocongosto import views
from appcastillocongosto.views import *

# servicio de ficheros estáticos durante el desarrollo
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
# servicio de ficheros estáticos durante el servidor
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('castillo/', views.castillo,name='castillo'),
    path('sobremi/', views.sobremi,name='sobremi'),
    path('Login/', views.Login, name='Login'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('descargar_pdf/<str:filename>/', views.descargar_pdf, name='descargar_pdf'),
    path('mostrar_pdf/<str:filename>/', views.mostrar_pdf, name='mostrar_pdf'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
