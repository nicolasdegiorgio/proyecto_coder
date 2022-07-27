#Con esto me evito que el archivo principal de urls se llene de lineas

from django.urls import path
from coder.views import *

urlpatterns = [
    path('', inicio),
    path('cursos/', lista_cursos),
    path('estudiante/', estudiante),
    path('profesores/', profesor),
    path('entregables/', entregable)
]

