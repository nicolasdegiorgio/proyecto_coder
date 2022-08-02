#Con esto me evito que el archivo principal de urls se llene de lineas

from django.urls import path
from coder.views import *

urlpatterns = [
    path('', inicio , name = 'index'),
    path('cursos/', lista_cursos , name = 'cursos'),
    path('estudiante/', estudiante, name = 'estudiante'),
    path('profesores/', profesor),
    path('entregables/', entregable)
]

