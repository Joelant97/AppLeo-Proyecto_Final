from django.http import HttpResponse
from django.template import loader
from .models import Evaluacion


def index(request):
    all_evaluaciones = Evaluacion.objects.all()
    template = loader.get_template('resources/index.html')
    context = {
        'all_evaluaciones': all_evaluaciones,
    }
    return HttpResponse(template.render(context, request))


#Los request conectan las WebPages, Imagenes o lo que sea.
def detalles(request, evaluacion_id):
    return HttpResponse("<h2>Detalles por Evaluaciones ID: " + str(evaluacion_id) + "</h2>")



