from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Esta es la Home-Pages de las Evaluaciones")


