from django.contrib import admin
from coder.models import Curso
# Register your models here.
#Agregamos modelos para administrar desde el panel de administracion

admin.site.register(Curso)

#Despues de esto se pueden administrar desde el panel
#Probar como cargar datos desde el panel