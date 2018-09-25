from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Evaluacion


def index(request):
    all_evaluaciones = Evaluacion.objects.all()
    return render(request, 'resources/index.html', {'all_evaluaciones': all_evaluaciones})


#Los request conectan las WebPages, Imagenes o lo que sea.
def detalles(request, evaluacion_id):
    evaluacion = get_object_or_404(Evaluacion, pk=evaluacion_id)
    return render(request, 'resources/detalles.html', {'evaluacion': evaluacion})

