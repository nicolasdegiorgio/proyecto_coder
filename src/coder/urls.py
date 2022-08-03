#Con esto me evito que el archivo principal de urls se llene de lineas

from django.urls import path
from coder.views import *

urlpatterns = [
    path('', inicio , name = 'index'),
    path('cursos/', lista_cursos , name = 'cursos'),
    path('estudiante/', estudiante, name = 'estudiante'),
    path('profesores/', profesor),
    path('entregables/', entregable),
    path('entregables/', entregable),
    path('formulario/', formulario),
    path('infoformulario/', info_formulario, name="infoformulario"),
    path('cursos/crear', crear_curso, name="crearcurso"),
    path('login/', fake_login, name="login falso"),
]

