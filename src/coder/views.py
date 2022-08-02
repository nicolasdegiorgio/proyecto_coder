from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from coder.models import Curso, Estudiante, Profesor, Entregable
# Create your views here.

def lista_cursos(request):  #Se va a realizar una herencia desde index hacia el template
    
    
    cursos = Curso.objects.all()
    
    lista_cursos_nombres=[]
    
    for curso in cursos:
        lista_cursos_nombres.append(curso.nombre)

    
    context = {
        'mensaje': 'Bienvenid@s',
        'mensaje_bienvenida':'Esta es la comision 40150',
        'listado_cursos': lista_cursos_nombres
    }
    return render(request, 'coder/cursos.html',context)
    

def inicio(request):
    return render(request, 'coder/index.html',{'mensaje':'esto es un proyecto coder'})


def estudiante(request):
    return HttpResponse('Vista de estudiante')


def profesor(request):
    return HttpResponse('Vista de profesor')


def entregable(request):
    return HttpResponse('Vista de entregable')
