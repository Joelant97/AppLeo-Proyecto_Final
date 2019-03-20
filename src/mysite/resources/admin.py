from django.contrib import admin
from .models import Estudiante
from .models import Evaluacion
from .models import Fluidez
from .models import Comprension
from .models import Profesor
#from .models import EvaluacionForm

# Registre los Modelos aqui.

admin.site.register(Estudiante)
admin.site.register(Evaluacion)
admin.site.register(Fluidez)
admin.site.register(Comprension)
admin.site.register(Profesor)
#admin.site.register(EvaluacionForm)


#Para registrar el modelo Profesor en el admin de django editamos nuestro admin.py
# @admin.register(Profesor)
# class ProfesorAdmin(admin.ModelAdmin):
#     list_display = ('usuario', 'direccion', 'telefono')
