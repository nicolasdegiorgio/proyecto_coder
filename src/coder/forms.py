#creamos este archivo para crear formularios de manera más sencilla
from django.forms import Form, CharField, IntegerField


class CursoFormulario (Form):
    
    nombre = CharField()
    camada = IntegerField()
    