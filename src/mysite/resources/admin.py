from django.contrib import admin
from .models import Profesor
from .models import Estudiante
from .models import Evaluacion
from .models import Fluidez
from .models import Comprension

# Registre los Modelos aqui.

admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Evaluacion)
admin.site.register(Fluidez)
admin.site.register(Comprension)
