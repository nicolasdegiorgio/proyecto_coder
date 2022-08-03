from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from coder.models import Curso, Estudiante, Profesor, Entregable
from coder.forms import CursoFormulario
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

def formulario(request):
    return render (request, 'coder/formulario.html')

#Definimos la ruta para recibir la informacion de los get y post del html
def info_formulario(request):
    print (request.method)
    return HttpResponse(f'Acceso confirmado')

def crear_curso(request):
    
    if request.method == "GET":
        formulario = CursoFormulario()
        return render(request, 'coder/formulario.html', {'formulario': formulario})
    else:
        nombre = request.POST['nombre']
        camada = request.POST['camada']
        curso= Curso(nombre=nombre, camada=camada)
        
        curso.save()
        return render(request, 'coder/index.html')
    
    
    
    
    
def fake_login(request):
    
    
    if request.method == "GET":
        return render(request, "coder/login.html")
    else:
        username = request.POST["username"]
        password = request.POST["password"]

        if username == "admin" and password == "12345":
            return HttpResponse("Bienvenido Admin")
        else:
            return HttpResponse("No te conozco")

