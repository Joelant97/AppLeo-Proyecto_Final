from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Esta es la Home-Pages de las Evaluaciones</h1>")


#Los request conectan las WebPages, Imagenes o lo que sea.
def detalles(request, evaluacion_id):
    return HttpResponse("<h2>Detalles por Evaluaciones ID: " + str(evaluacion_id) + "</h2>")



