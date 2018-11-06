from django.contrib import admin
from .models import Estudiante
from .models import Evaluacion
from .models import Fluidez
from .models import Comprension
from .models import EvaluacionForm

# Registre los Modelos aqui.

admin.site.register(Estudiante)
admin.site.register(Evaluacion)
admin.site.register(Fluidez)
admin.site.register(Comprension)
admin.site.register(EvaluacionForm)