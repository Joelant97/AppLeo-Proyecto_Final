from django.http import Http404
from django.shortcuts import render
from .models import Evaluacion


def index(request):
    all_evaluaciones = Evaluacion.objects.all()
    return render(request, 'resources/index.html', {'all_evaluaciones': all_evaluaciones})


#Los request conectan las WebPages, Imagenes o lo que sea.
def detalles(request, evaluacion_id):
    try:
        evaluacion = Evaluacion.objects.get(pk=evaluacion_id)
    except Evaluacion.DoesNotExist:
        raise Http404("La evaluacion no existe o no ha sido encontrada por el Servidor.")
    return render(request, 'resources/detalles.html', {'evaluacion': evaluacion})







